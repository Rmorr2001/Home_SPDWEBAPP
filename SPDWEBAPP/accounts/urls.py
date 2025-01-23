from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_home),
    path('login/', views.login_view, name= 'login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('roster/', views.roster, name='roster'),

    path('logout/', views.logout, name='logout'),


    path('dashboard/edit_dashboard_links/', views.edit_dashboard_links),
]