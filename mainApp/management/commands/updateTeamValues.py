# nba-api
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.endpoints import leaguestandingsv3
# django
from mainApp.models import Team

# python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
import datetime
from time import sleep

# Command
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Updates A teams market price depending on if they won the game on the day the command is run'
    
    def handle(self, *args, **kwargs):
        db_teams = Team.objects.all()
        for team in db_teams:
            ## THE PORTLAND TRAILBLAZERS REFUSE TO COMFORM TO THIS API, THEY REQUIRE HARD CODED CHANGING FOR LEAGUE STANDING

            # update team rankings
            s = leaguestandingsv3.LeagueStandingsV3(season="2020") # hard coded season value
            standings = s.get_data_frames()[0]

            team_name = str(team.full_name).split(" ")[-1]
            #logging.debug(team_name)
            curTeam = standings.loc[standings["TeamName"] == team_name]

            # check if empty 
            if curTeam.empty:
                pass
            else:
                team.league_standing = curTeam.PlayoffRank.values[0]
                team.conference = curTeam.Conference.values[0]
                team.save()


            # ''' INITIAL EVALUTAION ''' (uncomment if you need to reset team values)
            '''
            team.market_price = (50 - (2 * team.league_standing))
            team.save()
            '''

            # ''' EVALUTAION '''        

            api_team = [t for t in teams.get_teams() if t['abbreviation'] == str(team.slug)][0]
            team_id = api_team['id']
            
            today = str(datetime.datetime.today().strftime('%m/%d/%Y'))
            yesterday = str( (datetime.datetime.today() - datetime.timedelta(days=1) ).strftime('%m/%d/%Y'))

            gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id, date_from_nullable=today, date_to_nullable=today)
            game = gamefinder.get_data_frames()[0]

            # team did not have a game today
            if game.empty:
                continue

            # Win Lose Evaluation
            win_value = 1.5
            temp_odds = 1.5
            net_value = 0
            logging.debug(game)

            # Find opposing team's standing 
            at_team_slug = str(game['MATCHUP'].values[0])[-3:]
            at_team = Team.objects.get(slug=at_team_slug)
            at_team_standing = at_team.league_standing

            win_lose = game['WL'][0]
            
            if win_lose == 'W':
                net_value += ( (team.league_standing / 7.5) * win_value ) * temp_odds
            else:
                net_value -= ( (at_team_standing / 7.5) * win_value) * temp_odds
            
            team.market_price += net_value
            team.save()
            logging.debug('Team Updated:' + team.full_name + ' Net value:' + str(net_value))
            
            
            sleep(10)
