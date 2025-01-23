from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Brother(models.Model):
    STATUS = (
        ('New Member', 'New Member'),
        ('Active', 'Active'),
        ('Active Exec', 'Active Exec'),
        ('Pledge Board', 'Pledge Board'),
        ('Alumni','Alumni'),
        ('Alumni Exec','Alumni Exec'),
        )
    
    SEMESTER = (
        ('Fall', 'Fall'),
        ('Spring', 'Spring'),
        )

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    brother_name = models.CharField(max_length=200, null=True)
    birthday = models.CharField(max_length=200, null=True, blank=True) #I want people to be able to pick from a calendar
    email = models.CharField(max_length=200, null=True, blank=True)
    hometown = models.CharField(max_length=200, null=True, blank=True) #I would like people to be able to choose from an existing list, or create their own # I would probably just have to import a tuples-tuple that somehow gets updated
    phone_number = models.CharField(max_length=200, blank=True)
    major = models.CharField(max_length=200, null=True, blank=True) #choice #Same as hometown, I would like a list that we can add to... This might be a tag function!
    rush_semester = models.CharField(max_length=200, null=True, choices=SEMESTER, blank=True) #choice of spring or fall
    rush_year = models.CharField(max_length=200, null=True, blank=True) #choice of year up until 2100 
    grad_semester = models.CharField(max_length=200, null=True, choices=SEMESTER, blank=True) #choice of spring or fall
    grad_year = models.CharField(max_length=200, null=True, blank=True) #choice of year up until 2100 
    membership_status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True)
    #Profile picture?
    #Class as a Tag?


    def __str__(self):
        return self.brother_name
    

class Dashboard_Link(models.Model):
    STATUS = (
        ('New Member', 'New Member'),
        ('Active', 'Active'),
        ('Active Exec', 'Active Exec'),
        ('Pledge Board', 'Pledge Board'),
        ('Alumni','Alumni'),
        ('Alumni Exec','Alumni Exec'),
        )
    dashboard_redirect_name = models.CharField(max_length=200, null=True)
    redirect = models.CharField(max_length=200, null=True)
    membership_status = models.CharField(max_length=200, null=True, choices=STATUS)
    #Who_Changed_It = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.dashboard_redirect_name

