from telnetlib import LOGOUT
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, "home.html")
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

def history(request):
    return render(request, "history.html")

def chat(request):
    return render(request, "chat.html")

def about(request):
    return render(request, "about.html")
