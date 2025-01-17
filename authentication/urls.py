from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views 
urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('signin', views.signin, name='signin'),
    path('l', views.l, name='l'),
    path('lost', views.lost, name='lost'),
    path('found', views.found, name='found'),
    path('signout', views.signout, name='signout'),
    # Add the following two lines for lost.html and found.html
    path('lost.html', views.lost, name='lost-html'),  # Add a comma here
    path('found.html', views.found, name='found-html'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('l.html', views.l, name='l'),\
    path('saveenqiry', views.saveenqury, name="saveenqiry"),
    path('save_lost_item', views.save_lost_item, name="save_lost_item"),
    path('save_found_item', views.save_found_item, name="save_found_item"),
    path('thank_you', views.thank_you, name='thank_you'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='about'),
    

    path('response', views.response, name='response'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),

    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
