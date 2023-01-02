from django.shortcuts import render
from App import forms
from django.contrib.auth.decorators import login_required
from App.forms import SignUpForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import logout

# Create your views here.

def homepage(request):
    return render(request, 'App/homepage.html')

def aboutus(request):
    return render(request,'App/aboutuspage.html');

@login_required
def bookevent_view(request):
    sentdata = False
    formObj=forms.BookeventForm();
    if request.method=="POST":
        formObj=forms.BookeventForm(request.POST)
        if formObj.is_valid():
            print('Given or Submitted Form data..!!')
            print('username:', formObj.cleaned_data['username'])
            print('EventName:', formObj.cleaned_data['EventName'])
            formObj.save(commit=True)
            sentdata = True;
            formObj = forms.BookeventForm();
    return render(request, 'APP/eventbookform.html', {"form1":formObj, 'sentdata':sentdata });

def logout_view(request):
    return render(request,'registration/logout.html')


# def log_out(request):
#     logout(request)
#     messages.info(request, 'you have logout successfully')
#     return redirect('index', foo='bar')

def signup_view(request):
    formobj=SignUpForm()
    if request.method=="POST":
        formobj=SignUpForm(request.POST)
        user=formobj.save()
        user.set_password(user.password) #it applies pwd-hashers
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'App/signup.html', {'formobj':formobj})

def login_view(request):
    return render(request,'registration/login.html')



