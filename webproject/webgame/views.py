from telnetlib import LOGOUT
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import registerform, loginform
from .models import  Member
# Create your views here.
def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == 'POST':
        details = registerform(request.POST)
        member = Member()
        member.firstname = details['first_name'].value()
        member.lastname = details['last_name'].value()
        member.password = details['password'].value()

        member.save()
        return redirect("/admin") 
    else:
        context={}
        context['form'] = registerform()
    return render(request, "register.html",context=context)

#ตั้งชื่อfunctionได้ตามสะดวก

def LoginView(request):
    if request.method == 'POST':
        member = Member()
        user_firstname = member.objects.get(member.firstname)
        user_lastname = member.objects.get(member.lastname)
        user_password = member.objects.get(member.password)
        if user_firstname:
            if user_password:
                messages.info(request, "")
                request.session['fname'] = user_firstname.firstname
                request.session['lname'] = user_lastname.lastname
                return render(request, "login.html")
            if user_password is not None:
                messages.info(request, "รหัสผ่านไม่ถูกต้อง") 
        if user_firstname is not None:
            messages.info(request, "ชื่อไม่ถูกต้อง") 
    else:
        context={}
        context['form'] = loginform()
    return render(request, "login.html",context=context)

def LogoutView(request):
    del request.session['fname']
    del request.session['fname']
    #แจ้งว่าlogoutแล้ว แก้ messageได้
    messages.info(request, "Logged out successfully!")
    return redirect("/home") #logoutแล้วไปหน้าที่เรากำหนด แก้ได้

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
