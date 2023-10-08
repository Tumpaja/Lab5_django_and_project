from django.shortcuts import render
  
# Create your views here.
def home(request):
    return render(request, "home.html")

def signup(request):
    return render(request, "signup.html")

def login(request):
    return render(request, "login.html")

def news(request):
    return render(request, "news.html")

def history(request):
    return render(request, "history.html")

def chat(request):
    return render(request, "chat.html")

def about(request):
    return render(request, "about.html")
