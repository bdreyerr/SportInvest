from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
from mainApp.models import Team
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
import datetime
from time import sleep
# Command
from django.core.management.base import BaseCommand, CommandError
# For each team in database
#   if team won last game
        # increase market_value by 1
#   else    
#       # decrease market_value by 1

class Command(BaseCommand):
    help = 'Updates A teams market price depending on if they won the game on the day the command is run'
    
    def handle(self, *args, **kwargs):
        db_teams = Team.objects.all()
        for team in db_teams:
            api_team = [t for t in teams.get_teams() if t['abbreviation'] == str(team.slug)][0]
            team_id = api_team['id']
            
            today = str(datetime.datetime.today().strftime('%m/%d/%Y'))
            yesterday = str( (datetime.datetime.today() - datetime.timedelta(days=1) ).strftime('%m/%d/%Y'))

            gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id, date_from_nullable=today, date_to_nullable=today)
            game = gamefinder.get_data_frames()[0]
            # team did not have a game today
            if game.empty:
                continue
            logging.debug(game)
            win_lose = game['WL'][0]
            
            
            if win_lose == 'W':
                team.market_price += 0.5
            else:
                team.market_price -= 0.5
            logging.debug('Team Updated:' + team.full_name)
            
            team.save()
            sleep(10)
