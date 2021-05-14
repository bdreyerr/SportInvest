
import logging
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from mainApp.models import UserValueTimestamp, TeamValueTimestamp

from datetime import datetime, timedelta

class Command(BaseCommand):

    def clearStamps(self, stamps, time_frame):
        stack = []
        for stamp in stamps:
            cur_time = stamp.timestamp
            if not stack:
                stack.append(stamp)
            else:
                last_time = stack[-1].timestamp
                difference  = abs(cur_time - last_time)
                #logging.debug(difference)
                if difference.total_seconds() < time_frame:
                    stamp.delete()
                else:
                    stack.append(stamp)


    def handle(self, *args, **kwargs):
        date_from = None
        date_to = datetime.now()
        logging.debug("Cleaning Timestamps")

        # seperate todays stamps by 60 seconds        
        date_from = date_to + timedelta(hours=-24)
        user_stamps_day = UserValueTimestamp.objects.filter(timestamp__range=(date_from, date_to)).order_by("timestamp").reverse()
        team_stamps_day = TeamValueTimestamp.objects.filter(timestamp__range=(date_from, date_to)).order_by("timestamp").reverse()
        self.clearStamps(user_stamps_day, 60)
        self.clearStamps(team_stamps_day, 60)
        
        # seperate this weeks stamps by 15 minutes
        date_from = date_to + timedelta(days=-7)
        user_stamps_week = UserValueTimestamp.objects.filter(timestamp__range=(date_from, date_to)).order_by("timestamp").reverse()
        team_stamps_week = TeamValueTimestamp.objects.filter(timestamp__range=(date_from, date_to)).order_by("timestamp").reverse()
        self.clearStamps(user_stamps_week, 60 * 15)
        self.clearStamps(team_stamps_week, 60 * 15)


        # seperte this months stamps by 6 hours
        date_from = date_to + timedelta(days=-30)
        user_stamps_month = UserValueTimestamp.objects.filter(timestamp__range=(date_from, date_to)).order_by("timestamp").reverse()
        team_stamps_month = TeamValueTimestamp.objects.filter(timestamp__range=(date_from, date_to)).order_by("timestamp").reverse()
        self.clearStamps(user_stamps_month, (60* 360))
        self.clearStamps(team_stamps_month, (60* 360))

        # seperate this years stamps by 24 hours
        date_from = date_to + timedelta(days=-365)
        user_stamps_year = UserValueTimestamp.objects.filter(timestamp__range=(date_from, date_to)).order_by("timestamp").reverse()
        team_stamps_year = TeamValueTimestamp.objects.filter(timestamp__range=(date_from, date_to)).order_by("timestamp").reverse()
        self.clearStamps(user_stamps_year, (60* 1440))
        self.clearStamps(team_stamps_year, (60* 1440))