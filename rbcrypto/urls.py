from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('private/user/signupwithemail', views.signupwithemail, name='signupwithemail'),
    path('private/user/signupwithgoogle', views.signupwithgoogle, name='signupwithgoogle'),
    path('private/user/addtowatchlist', views.addtowatchlist, name='addtowatchlist'),
    path('private/user/getwatchlistinfo', views.getwatchlistinfo, name='getwatchlistinfo')
]