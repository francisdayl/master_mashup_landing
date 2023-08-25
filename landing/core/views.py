from django.shortcuts import render
from .models import Email
from .forms import NewEmailForm
# Create your views here.

app_name = 'core'

def index(request):
    cosas = []
    form = NewEmailForm()

    return render(request, 'core/index.html',{'cosas':cosas, 'form':form})

def new(request):
    form = NewEmailForm()
    
    
    return render(request, 'core/')


