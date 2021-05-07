from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput, Textarea, NumberInput
from mainApp.models import Transaction


class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
    first_name = forms.CharField(label='First Name', max_length=20, required=True)
    last_name = forms.CharField(label='Last Name', max_length=20, required=True)
    username = forms.CharField(label='Username', max_length=20, required=True)
    email = forms.EmailField(label='Email', max_length=30, required=True)
    password1 = forms.CharField(widget=PasswordInput(attrs={'placeholder':''}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'placeholder':''}))

class Login(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': ''}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':''}))






class TradeTeam(forms.ModelForm):    
    class Meta:
        model = Transaction
        fields = ('trade_choice', 'num_shares',)
    def __init__(self, *args, **kwargs):
        super(TradeTeam,self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = True
        self.fields['trade_choice'].label="Trade Choice"
        self.fields['num_shares'].label="No. Shares"
        self.fields['num_shares'].widget.attrs['placeholder'] = 0

    def clean(self):
        cleaned_data = super().clean()
        num_shares = cleaned_data.get('num_shares')

        if num_shares <= 0:
            msg = "No. of shares must be greater than 0"
            self.add_error('num_shares', msg)
