from django import forms
from App.models import Event
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date';

class BookeventForm(forms.ModelForm):
    EventDate = forms.DateField(widget=DateInput());
    class Meta:
        model = Event;
        fields = '__all__';

class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=26)
    password = forms.CharField(widget=forms.PasswordInput)
    email= forms.EmailField()

    class Meta:
        model=User		#it is mysql-db model-table(for auth_app_db)
        fields=['username', 'password','email'];