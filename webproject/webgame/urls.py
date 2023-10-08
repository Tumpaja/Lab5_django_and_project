from django.contrib import admin
from django.conf.urls import url
  
# importing views from views..py
from .views import home, RegisterUserView, LoginView, LogoutView, news, history, chat, about

urlpatterns = [
    url(r'^admin$', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^Register$', RegisterUserView, name='RegisterUserView'),
    url(r'^Login$', LoginView, name='LoginView'),
    url(r'^Logout$', LogoutView, name='LogoutView'),
    url(r'^news$', news, name='news'),
    url(r'^history$', history, name='history'),
    url(r'^chat$', chat, name='chat'),
    url(r'^about$', about, name='about'),
]