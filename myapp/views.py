from django.shortcuts import render
from myapp.models import *
# Create your views here.

def index(request):
    obj=imageupload.objects.all()
    return render(request, 'index.html',{'data':obj})