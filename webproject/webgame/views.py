from telnetlib import LOGOUT
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from .forms import loginform
from .models import Choice
# Create your views here.
def home(request):
    return render(request, "home.html")

def login(request):
    if request.method == 'POST':
        details = loginform(request.POST)
        print(details['first_name'].value())
    context={}
    context['form'] = loginform()
    return render(request, "login.html",context=context)

#ตั้งชื่อfunctionได้ตามสะดวก
def RegisterUserView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #เมื่อสมัครเสร็จแล้วจะให้เด้งไปหน้าไหน
            return redirect("/admin")

        #เพื่อแจ้งเตือน errorต่างๆ
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "register.html",
                          context={"form":form}) #นำ form ตรงนี้ไปใช้ใน register.htmlเพื่อrender

    #เนื่อจากข้างบนเป็น if-elseเลยต้องมีเผื่อไว้
    form = UserCreationForm
    return render(request = request,
                  template_name = "register.html",
                  context={"form":form})

def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            #เช็คความถูกต้อง
            if user is not None: 
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/admin')#loginเสร็จแล้วไปที่หน้า /admin แก้เป็นหน้าอื่นได้เช่น /home
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form}) 

def LogoutView(request):
    LOGOUT(request)
    #แจ้งว่าlogoutแล้ว แก้ messageได้
    messages.info(request, "Logged out successfully!")
    return redirect("/admin") #logoutแล้วไปหน้าที่เรากำหนด แก้ได้

def news(request):
    return render(request, "news.html")
def game(request):
    return render(request, "game.html")
def chat(request):
    return render(request, "chat.html")
def about(request):
    return render(request, "about.html")
def n1(request):
    return render(request, "n1.html")
def n2(request):
    return render(request, "n2.html")
def n3(request):
    return render(request, "n3.html")
def n4(request):
    return render(request, "n4.html")
def n5(request):
    return render(request, "n5.html")
def n6(request):
    return render(request, "n6.html")
def n7(request):
    return render(request, "n7.html")
def n8(request):
    return render(request, "n8.html")
def n9(request):
    return render(request, "n9.html")
def n10(request):
    return render(request, "n10.html")

def g1(request):
    return render(request, "g1.html")
def g2(request):
    return render(request, "g2.html")
def g3(request):
    return render(request, "g3.html")
def g4(request):
    return render(request, "g4.html")
def g5(request):
    return render(request, "g5.html")
def g6(request):
    return render(request, "g6.html")
def g7(request):
    return render(request, "g7.html")
def g8(request):
    return render(request, "g8.html")
def g9(request):
    return render(request, "g9.html")
def g10(request):
    return render(request, "g10.html")
def g11(request):
    return render(request, "g11.html")
def g12(request):
    return render(request, "g12.html")
def g13(request):
    return render(request, "g13.html")
def g14(request):
    return render(request, "g14.html")
def g15(request):
    return render(request, "g15.html")
def g16(request):
    return render(request, "g16.html")
def g17(request):
    return render(request, "g17.html")
def g18(request):
    return render(request, "g18.html")
def g19(request):
    return render(request, "g19.html")
def g20(request):
    return render(request, "g20.html")
