from django.contrib import admin
from django.urls import path,include,re_path
from django.urls import re_path as url
  
# importing views from views..py
from .views import (home,home2, register, LoginView, LogoutView, news, game, chat, about, 
                    n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10,
                    g11, g12, g13, g14, g15, g16, g17, g18, g19, g20,
)
urlpatterns = [
    url(r'^admin$', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^$', home2, name='home2'),
    url(r'^register$', register, name='register'),
    
    url(r'^Login$', LoginView, name='LoginView'),
    url(r'^Logout$', LogoutView, name='LogoutView'),
    
    url(r'^news$', news, name='news'),
    url(r'^game$', game, name='game'),
    url(r'^chat$', chat, name='chat'),
    url(r'^aboutus$', about, name='about'),
    url(r'^news/news1$', n1, name='n1'),
    url(r'^news/news2$', n2, name='n2'),
    url(r'^news/news3$', n3, name='n3'),
    url(r'^news/news4$', n4, name='n4'),
    url(r'^news/news5$', n5, name='n5'),
    url(r'^news/news6$', n6, name='n6'),
    url(r'^news/news7$', n7, name='n7'),
    url(r'^news/news8$', n8, name='n8'),
    url(r'^news/news9$', n9, name='n9'),
    url(r'^news/news10$', n10, name='n10'),
    url(r'^game/game1$', g1, name='g1'),
    url(r'^game/game2$', g2, name='g2'),
    url(r'^game/game3$', g3, name='g3'),
    url(r'^game/game4$', g4, name='g4'),
    url(r'^game/game5$', g5, name='g5'),
    url(r'^game/game6$', g6, name='g6'),
    url(r'^game/game7$', g7, name='g7'),
    url(r'^game/game8$', g8, name='g8'),
    url(r'^game/game9$', g9, name='g9'),
    url(r'^game/game10$', g10, name='g10'),
    url(r'^game/game11$', g11, name='g11'),
    url(r'^game/game12$', g12, name='g12'),
    url(r'^game/game13$', g13, name='g13'),
    url(r'^game/game14$', g14, name='g14'),
    url(r'^game/game15$', g15, name='g15'),
    url(r'^game/game16$', g16, name='g16'),
    url(r'^game/game17$', g17, name='g17'),
    url(r'^game/game18$', g18, name='g18'),
    url(r'^game/game19$', g19, name='g19'),
    url(r'^game/game20$', g20, name='g20'),
]