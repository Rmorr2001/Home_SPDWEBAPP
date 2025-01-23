from django.forms import ModelForm
from .models import *

class DashboardLinkForm(ModelForm):
    class Meta:
        model = Dashboard_Link
        fields = '__all__'