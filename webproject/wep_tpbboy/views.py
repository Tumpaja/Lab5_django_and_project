from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'E:\Project\GitHub\Lab5_django_and_project\webproject\wep_tpbboy\web\index.html')
    #return HttpResponse("Hello, world!")