from django.contrib import admin
from mainApp.models import Team, Transaction, Profile, UserOwnedTeam, UserValueTimestamp, TeamValueTimestamp
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'market_price', 'description', 'share_holders', 'bg_image']
admin.site.register(Team, TeamAdmin)

class TransactionAdmin(admin.ModelAdmin):
    fields = ['user', 'team', 'trade_choice', 'num_shares', 'trade_price', 'trade_value']
admin.site.register(Transaction, TransactionAdmin)

class ProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'portfolio_value', 'total_value', 'buying_power']
admin.site.register(Profile, ProfileAdmin)

class UserTeamAdmin(admin.ModelAdmin):
    fields = ['user', 'team', 'num_shares', 'average_cost']
admin.site.register(UserOwnedTeam, UserTeamAdmin)

class TimeStampAdmin(admin.ModelAdmin):
    fields = ['user', 'value', 'timestamp']
admin.site.register(UserValueTimestamp, TimeStampAdmin)

class TeamTimeStampAdmin(admin.ModelAdmin):
    fields = ['team', 'value', 'timestamp']
admin.site.register(TeamValueTimestamp, TeamTimeStampAdmin)