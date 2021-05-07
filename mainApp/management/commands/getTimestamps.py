from mainApp.models import Team, Transaction, UserOwnedTeam, UserValueTimestamp, TeamValueTimestamp
from django.contrib.auth import get_user_model
import datetime

# Command
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Creates Objects saving the current portfolio value of each user, and market price of each time'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        users = User.objects.all()
        for user in users:
            try:
                portfolio_value = user.profile.portfolio_value
            except:
                portfolio_value = 0.00001
            userTimestamp = UserValueTimestamp(user=user, value=portfolio_value, timestamp=datetime.datetime.now())
            userTimestamp.save()

        teams = Team.objects.all()
        for team in teams:
            teamTimestamp = TeamValueTimestamp(team=team, value=team.market_price, timestamp=datetime.datetime.now())
            teamTimestamp.save()
        self.stdout.write(self.style.SUCCESS('Successfully saved all values'))