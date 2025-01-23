from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_home(request):
    return redirect('dashboard/')

def login_view(request):
    #NEEDS A WRAP DECORATOR TO WORK
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('it posted')
        user = authenticate(request, username = username, password= password)
        if user is not None:
            login(request, user)
            print('it worked')
            return redirect('dashboard')
        else:
            return redirect('home')
    context = {}
    print(request.user)
    return render(request, 'accounts/login.html',context)

def logoutuser(request):
    logout(request)
    return redirect('login')

def edit_dashboard_links(request):
    
    form = DashboardLinkForm()
    if request == 'POST':
        form = DashboardLinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'active_links':Dashboard_Link.objects.all(),'form':form,}
    return render(request, 'accounts/dashboard/edit_dashboard.html', context)

def edit_dashboard_links(request):
    
    form = DashboardLinkForm()
    if request == 'POST':
        form = DashboardLinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'active_links':Dashboard_Link.objects.all(),'form':form,}
    return render(request, 'accounts/dashboard/edit_dashboard.html', context)

def dashboard(request):
    user_status = request.user.brother.membership_status
    if user_status == "Active Exec":
        context = {'active_links':Dashboard_Link.objects.all()}
        return render(request, 'accounts/dashboard/dashboard.html', context)
    if user_status == "New Member":
        context = {'active_links':Dashboard_Link.objects.filter(membership_status="New Member")}
        return render(request, 'accounts/dashboard/dashboard.html', context)
        #return render(requst, accounts/dashboard_activeadmin)
    #if some field is = blank
        #redirect to an html with a profile creation form
    #based off the user id direct to a different pag

    return HttpResponse(user_status)

def roster(request):
    list_of_brothers = Brother.objects.all()
    active_brother_count = Brother.objects.filter(membership_status = "Active Exec").count() + Brother.objects.filter(membership_status = "Active").count()
    alumni_brother_count = Brother.objects.filter(membership_status = "Alumni Exec").count() + Brother.objects.filter(membership_status = "Alumni").count()
    newmember_brother_count = Brother.objects.filter(membership_status = "New Member").count()

    context = {'list_of_brothers':list_of_brothers, "active_brother_count":active_brother_count, "alumni_brother_count":alumni_brother_count, "newmember_brother_count":newmember_brother_count}
    return render(request, 'accounts/roster.html', context)
    