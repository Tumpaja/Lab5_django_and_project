from django.contrib import admin
from django.conf.urls import url
  
# importing views from views..py
from .views import home, signup, login, news, history, chat, about
  
urlpatterns = [
    url(r'^admin$', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^signup$', signup, name='signup'),
    url(r'^login$', login, name='login'),
    url(r'^news$', news, name='news'),
    url(r'^history$', history, name='history'),
    url(r'^chat$', chat, name='chat'),
    url(r'^about$', about, name='about'),
]