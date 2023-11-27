from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'web'
urlpatterns = [
  path('',views.index, name='index'), 
  path('contact',views.contact, name='contact'), 
  path('course',views.course, name='course'),
  path('course/<slug>/', views.course_detail, name='course_detail'),
  path('register',views.register, name='register'),
  path('event_register',views.event_register, name='event_register'),
  path('about',views.about, name='about'),
]
