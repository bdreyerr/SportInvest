# django
from sportSite.secret_keys import google_captcha_key, news_api_key
from django.shortcuts import render, redirect
from .forms import Register, Login, TradeTeam
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from .models import Team, Transaction, UserOwnedTeam, UserValueTimestamp, TeamValueTimestamp
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import forms
from django.core.management import call_command
from django.contrib import messages
from django.conf import settings


# rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# python 
import logging, datetime, requests, json, os
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')





# ''' USER AUTHENTICATION '''

def login_request(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            form = Login(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    logging.debug('User Logged in: ' , str(user.username))
                    messages.success(request, "Logged in")
                    return redirect('portfolio')
                else:
                    logging.error('user does not exist')
                    
            messages.error(request, "Invalid Username or Password")
    
    form = Login()
    return render(request=request,
            template_name='login.html', 
            context={'form':form, "recaptcha_key": google_captcha_key})

def logout_request(request):
    logout(request)
    return redirect('index')


def register(request):
    form = Register(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            login(request, user)
            return redirect('portfolio')
    return render(request=request,
            template_name='register.html', 
            context={'form': form, "recaptcha_key": google_captcha_key})


# ''' SITE CONTENT ''' 

date_fromDay = datetime.datetime.now()- datetime.timedelta(days=1)
date_fromWeek = datetime.datetime.now()- datetime.timedelta(days=7)
date_fromMonth = datetime.datetime.now()- datetime.timedelta(days=30)
date_fromYear = datetime.datetime.now()- datetime.timedelta(days=365)

class ChartData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,format=None):
        # get timestamps
        # switch statement for 1D, 1W, 1Y

        timestampsDay = UserValueTimestamp.objects.filter(user=request.user, timestamp__gte=date_fromDay).order_by('timestamp')
        timestampsWeek = UserValueTimestamp.objects.filter(user=request.user, timestamp__gte=date_fromWeek).order_by('timestamp')
        timestampsMonth = UserValueTimestamp.objects.filter(user=request.user, timestamp__gte=date_fromMonth).order_by('timestamp')
        timestampsYear = UserValueTimestamp.objects.filter(user=request.user, timestamp__gte=date_fromYear).order_by('timestamp')

        
        ''' Fill Day Chart Data '''
        chartdataDay = []
        labelsDay=[]
        for stamp in timestampsDay:
            
            chartdataDay.append(stamp.value)
            dt = stamp.timestamp
            format = '%m-%d %I:%M %p'
            label = dt.strftime(format)
            labelsDay.append(label)

        ''' Fill Week Chart Data '''
        chartdataWeek = []
        labelsWeek=[]
        for stamp in timestampsWeek:
            chartdataWeek.append(stamp.value)
            dt = stamp.timestamp
            format = '%m-%d %I:%M %p'
            label = dt.strftime(format)
            labelsWeek.append(label)

        ''' Fill Month Chart Data '''
        chartdataMonth = []
        labelsMonth=[]
        for stamp in timestampsMonth:
            chartdataMonth.append(stamp.value)
            dt = stamp.timestamp
            format = '%m-%d %I:%M %p'
            label = dt.strftime(format)
            labelsMonth.append(label)
        

        ''' Fill Year Chart Data '''
        chartdataYear = []
        labelsYear=[]
        for stamp in timestampsYear:
            chartdataYear.append(stamp.value)
            dt = stamp.timestamp
            format = '%m-%d %I:%M %p'
            label = dt.strftime(format)
            labelsYear.append(label)

        
        chartLabel = ""
        data ={
                     "labelsDay":labelsDay,
                     "labelsWeek":labelsWeek,
                     "labelsMonth":labelsMonth,
                     "labelsYear":labelsYear,
                     "chartLabel":chartLabel,
                     "chartdataDay":chartdataDay,
                     "chartdataWeek":chartdataWeek,
                     "chartdataMonth":chartdataMonth,
                     "chartdataYear":chartdataYear,
             }
        return Response(data)

class TeamChartData(APIView):
    # authenticate user
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request, format=None, *args, **kwargs):
        url = request.build_absolute_uri()
        full_url = str(url)
        slug = full_url[-4:].replace('/','')
        team = Team.objects.get(slug=slug)
        timestampsDay = TeamValueTimestamp.objects.filter(team=team, timestamp__gte=date_fromDay).order_by('timestamp')
        timestampsWeek = TeamValueTimestamp.objects.filter(team=team, timestamp__gte=date_fromWeek).order_by('timestamp')
        timestampsMonth = TeamValueTimestamp.objects.filter(team=team, timestamp__gte=date_fromMonth).order_by('timestamp')
        timestampsYear = TeamValueTimestamp.objects.filter(team=team, timestamp__gte=date_fromYear).order_by('timestamp')

        ''' Fill Day Chart Data '''
        chartdataDay = []
        labelsDay=[]
        for stamp in timestampsDay:
            chartdataDay.append(stamp.value)
            dt = stamp.timestamp
            format = '%m-%d %I:%M %p'
            label = dt.strftime(format)
            labelsDay.append(label)

        ''' Fill Week Chart Data '''
        chartdataWeek = []
        labelsWeek=[]
        for stamp in timestampsWeek:
            chartdataWeek.append(stamp.value)
            dt = stamp.timestamp
            format = '%m-%d %I:%M %p'
            label = dt.strftime(format)
            labelsWeek.append(label)

        ''' Fill Month Chart Data '''
        chartdataMonth = []
        labelsMonth=[]
        for stamp in timestampsMonth:
            chartdataMonth.append(stamp.value)
            dt = stamp.timestamp
            format = '%m-%d %I:%M %p'
            label = dt.strftime(format)
            labelsMonth.append(label)
        

        ''' Fill Year Chart Data '''
        chartdataYear = []
        labelsYear=[]
        for stamp in timestampsYear:
            chartdataYear.append(stamp.value)
            dt = stamp.timestamp
            format = '%m-%d %I:%M %p'
            label = dt.strftime(format)
            labelsYear.append(label)
        
        chartLabel = ""
        data ={
                     "labelsDay":labelsDay,
                     "labelsWeek":labelsWeek,
                     "labelsMonth":labelsMonth,
                     "labelsYear":labelsYear,
                     "chartLabel":chartLabel,
                     "chartdataDay":chartdataDay,
                     "chartdataWeek":chartdataWeek,
                     "chartdataMonth":chartdataMonth,
                     "chartdataYear":chartdataYear,
                     "slug": slug,
             }
        return Response(data)

def landing_page(request):
    return render(request=request,
            template_name='index.html', 
            context={})

@login_required(login_url='index')
def portfolio(request):

    # ``` USER INFORMATION ```
    try:
        user = request.user
        teams = UserOwnedTeam.objects.filter(user = user).order_by("market_value").reverse()
    except:
        teams = None

    # get user timestamp
    curStamp = UserValueTimestamp(user=user, value=user.profile.portfolio_value, timestamp=datetime.datetime.now())
    curStamp.save()

    # update user's portfolio value
    update_portfolio_value(user, teams)

    # get timestamps (Day, Week, Month, Year)
    timestamps_day = UserValueTimestamp.objects.filter(user=request.user, timestamp__gte=date_fromDay).order_by('timestamp')
    timestamps_week = UserValueTimestamp.objects.filter(user=request.user, timestamp__gte=date_fromWeek).order_by('timestamp')
    timestamps_month = UserValueTimestamp.objects.filter(user=request.user, timestamp__gte=date_fromMonth).order_by('timestamp')
    timestamps_year = UserValueTimestamp.objects.filter(user=request.user, timestamp__gte=date_fromYear).order_by('timestamp')


    # calculate portfolio's netGain for time period
    if not teams:
        net_gain_day, net_gain_week, net_gain_month, net_gain_year = {'value': 0, 'sign':'+'}, {'value': 0, 'sign':'+'}, {'value': 0, 'sign':'+'}, {'value': 0, 'sign':'+'}
    else:
        net_gain_day = calculate_net_gain(timestamps_day)
        net_gain_week = calculate_net_gain(timestamps_week)
        net_gain_month = calculate_net_gain(timestamps_month)
        net_gain_year = calculate_net_gain(timestamps_year)


    # ``` FIND YOUR TEAM ```
   
    return render(request=request,
            template_name='portfolio.html',
            context={'teams': teams, 'net_gain_day': net_gain_day, 
            'net_gain_week': net_gain_week, 
            'net_gain_month': net_gain_month, 
            'net_gain_year': net_gain_year, 
            }) 


@login_required(login_url='index')
def team_view(request, slug):

    # get reference to user and team
    user = request.user
    team = Team.objects.get(slug=slug)

    # Checks if user owns shares of current team
    try:
        userTeam = UserOwnedTeam.objects.get(user=user, team=team)
    except:
        userTeam = None

    # if user owns shares, calculate current market_value
    if userTeam:
        userTeam.market_value = userTeam.num_shares * team.market_price
        userTeam.save()
    
    # history of user's transactions with current team
    history = Transaction.objects.filter(user=user, team=team).order_by('date').reverse()
    form = TradeTeam(request.POST or None)

    # save timestamp when page loaded 
    timestamp = TeamValueTimestamp(team=team, value=team.market_price, timestamp=datetime.datetime.now())
    timestamp.save()

    if request.method == 'POST':
        if form.is_valid():
            # Clean Trade Choice (Buy/Sell), No. Shares from valid form
            trade_choice = form.cleaned_data.get('trade_choice')
            num_shares = form.cleaned_data.get('num_shares')

            if num_shares <= 0:
                form.add_error(None, 'Share number cannot be less than or equal to zero')
                logging.error('Shares cannot be zero')
            
            # create transaction
            total_price = team.market_price * num_shares
            new_transaction = Transaction(user=user, team=team, trade_choice=trade_choice, num_shares=num_shares, trade_price=team.market_price, trade_value=total_price)
            new_transaction.save()

            # Buying Shares
            if trade_choice == '1':
                
                if total_price > user.profile.buying_power:
                    logging.error("Insufficient Funds (user: " , str(user.username), ', team: ', str(team.full_name), ')')
                    messages.error(request, "Insufficient Funds to make this transaction, please check your buying power")
                else:
                    # if user does not already own stock
                    if not userTeam:
                        # Create new ownership object
                        userTeam = UserOwnedTeam(user=user, team=team, num_shares=num_shares, average_cost=team.market_price, market_value = total_price)
                        userTeam.transaction = new_transaction

                        # add user to teams owners list
                        team.share_holders.add(user)
                        
                        # Save ownership
                        userTeam.save() 
                        logging.debug("Transaction Completed: User: ", str(user.username), ', Trade type: ', str(trade_choice), ', No. Shares: ', str(num_shares), '(New Ownership)')

                    # user already owns shares of team
                    else:

                        userTeam.num_shares += num_shares
                        # calculate the new average cost of the owned stock
                        transactions = Transaction.objects.filter(user=user, team=team, trade_choice='1')
                        share_weight = 0
                        for transaction in transactions:
                            share_weight += transaction.trade_value 
                        userTeam.average_cost = share_weight / userTeam.num_shares
                        userTeam.total_return = userTeam.market_value - (userTeam.average_cost * userTeam.num_shares)
                        userTeam.save()
                        
                        logging.debug("Transaction Completed: User: ", str(user.username), ', Trade type: ', str(trade_choice), ', No. Shares: ', str(num_shares), '(Existing Ownership)')
                    # update user's buying power
                    user.profile.buying_power -= total_price

                    # update user's portfolio value
                    user.profile.portfolio_value += total_price
                    user.save()
                    messages.success(request, "You just purchased " + str(num_shares) + " share(s) of " +team.slug+ " for $" + str(team.market_price))

            # Selling Shares
            elif trade_choice == '2':

                if not userTeam:
                    logging.error("Transaction Error: User: ", str(user.username), ', Trade type: ', str(trade_choice), ', No. Shares: ', str(num_shares), '(Cannot sell un-owned stock)')
                    messages.error(request, "You do not own any shares of " + team.slug)
                
                else:
                    if num_shares > userTeam.num_shares:
                        logging.error('You do not own enough shares to make this transaction')
                        messages.error(request, "Insufficient No. shares owned, please retry")
                        return redirect("../../team/"+team.slug)

                    # subtract team_shares, delete if selling all shares
                    userTeam.num_shares -= num_shares
                    userTeam.save()
                    if userTeam.num_shares == 0:
                        userTeam.delete()
                    
                    user.profile.buying_power += total_price
                    user.profile.portfolio_value -= total_price
                    messages.success(request, "You just sold " + str(num_shares) + " share(s) of " +team.slug+ " for $" + str(team.market_price))
                    user.save()
            call_command('getTimestamps')
            return redirect("../../team/"+team.slug+'/')
            
    # fetch new about current team
    articles = fetch_news(team.full_name)

    return render(request=request,
            template_name='team_view.html',
            context={'team':team, 'form':form, 
            'userTeam': userTeam, 
            'history': history, 
            'articles': articles,
            "recaptcha_key": google_captcha_key})
    
@login_required(login_url='index')
def transactions(request):
    buys = Transaction.objects.filter(user=request.user, trade_choice='1').order_by("date").reverse()
    buy_paginator = Paginator(buys, 5)
    sells = Transaction.objects.filter(user=request.user, trade_choice='2').order_by("date").reverse()
    sell_paginator = Paginator(sells, 5)
    page = request.GET.get('page', 1)

    # pagination
    try:
        buy_list = buy_paginator.page(page)
        sell_list = sell_paginator.page(page)
    except PageNotAnInteger:
        buy_list = buy_paginator.page(1)
        sell_list = sell_paginator.page(1)
    except EmptyPage:
        buy_list = buy_paginator.page(buy_paginator.num_pages)
        sell_list = sell_paginator.page(sell_paginator.num_pages)
    return render(request=request,
        template_name='transactions.html',
        context={'buys': buy_list, 'sells': sell_list})


@login_required(login_url='index')
def banking(request):

    return render(request=request,
        template_name='banking.html',
        context={})

def market(request):


    highest_valued = Team.objects.order_by('-market_price')[:10]
    league_leaders = []
    all_teams = Team.objects.all()
    for team in all_teams:
        if team.league_standing <= 6:
            league_leaders.append(team)

    league_leaders.sort(key= lambda x: x.league_standing)
    #league_leaders = Team.objects.order_by("league_standing")[:12]

    east = Team.objects.filter(conference="East")
    west = Team.objects.filter(conference="West")
    
    return render(request=request,
        template_name='market.html',
        context={'highest_valued':highest_valued, 
                'league_leaders': league_leaders,
                'east_teams': east,
                'west_teams': west    })


def about(request):
    return render(request=request, template_name="about.html")


# ''' Modular functions '''

# Generate News Articles
def fetch_news(team_name):
    
    team_name.replace(' ', '')
    url = ('https://newsapi.org/v2/everything?'
       'q='+team_name+'&'
       'sortBy=popularity&'
       'apiKey='+news_api_key)

    response = requests.get(url)
    data = response.json()
    articles = []
    for article in data['articles']:
        articles.append(article)
    try:
        return articles[:6]
    except:
        return articles
    
def update_portfolio_value(user, owned_teams):
    # get total portfolio value
    cur_value = 0
    if owned_teams:
        for team in owned_teams:
            cur_value += team.market_value
        user.profile.portfolio_value = cur_value    
    else:
        user.profile.portfolio_value = 0
    user.save()

# Calculate net Gain
def calculate_net_gain(timestamps):
    n = len(timestamps)
    start, end = timestamps[0].value, timestamps[n-1].value
    if end == 0:
        end = 0.0000001
    netGain = {}
    netGain['value'] =  end - start
    netGain['percentage'] = (1 - (start/end)) * 100
    if netGain['value'] > 0:
        netGain['sign'] = '+' 
    else:
        netGain['sign'] = '-' 
    return netGain
