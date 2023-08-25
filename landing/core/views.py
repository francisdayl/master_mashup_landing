from django.shortcuts import render, redirect
from .models import Email
from .forms import NewEmailForm
from django.contrib import messages

# Create your views here.

app_name = 'core'

def index(request):
    cosas = []
    form = NewEmailForm()
    if request.method=="POST":
        form = NewEmailForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Email registered successfully")
            return redirect('/')
            
    return render(request, 'core/index.html',{'cosas':cosas, 'form':form})


