from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# When using this in a template: 
'''
<h2>{{ user.get_full_name }}</h2>
<ul>
  <li>Username: {{ user.username }}</li>
  <li>Location: {{ user.profile.portfolio_value }}</li>
</ul>'''
# Using in a view method:
'''
def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ips dolor s.'
    user.save()
'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_value = models.FloatField(default=0)
    buying_power = models.FloatField(default=500)
    total_value = models.FloatField(default=0)

    def __str__(self):
        return self.user.username
    


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=255, unique=True, default='NaN')
    market_price = models.FloatField(default=1.0)
    description = models.TextField(max_length=400, blank=True)
    share_holders = models.ManyToManyField(User, related_name="owners", blank=True)
    bg_image = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=None)
    
    class Meta:
        get_latest_by = 'market_price'

    def __str__(self):
        return self.name
    
    #def save(self, *args, **kwargs):
        #self.background_image_url= "background-image: linear-gradient(to top, rgba(46, 49, 65, 0.8), rgba(46, 49, 65, 0.8)), url( '{% static 'images/" +str(self.slug)+".jpg' %}' );"
    #    super(Subject, self).save(*args, **kwargs)
    
# Object created for every buy and sell
class Transaction(models.Model):
    CHOICES =(
    ("1", "Buy"),
    ("2", "Sell"),)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    trade_choice = models.CharField(max_length=300, choices=CHOICES)
    num_shares = models.FloatField(default=None)
    trade_price = models.FloatField(default=0)
    trade_value = models.FloatField(default=0)

    def __str__(self):
        return self.user.username+self.team.slug+self.trade_choice+str(self.num_shares)+str(self.date)


# instance created when a user buys a team 
# updated for each buy after initial buy
# (deleted when user sells all shares of the team)
class UserOwnedTeam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    num_shares = models.FloatField(default=0)
    average_cost = models.FloatField(default=0) # average cost of shares purchased
    market_value = models.FloatField(default=0) 
    total_return = models.FloatField(default=0)
    
    def __str__(self):
        return self.user.username + self.team.name


class UserValueTimestamp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.FloatField(default=0) # updated to the user's portfolio value every time corresponding script is run
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.user.username + ' UVT ' + str(self.timestamp)



class TeamValueTimestamp(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    value = models.FloatField(default = 0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.team.name + ' TVT ' + str(self.timestamp)


