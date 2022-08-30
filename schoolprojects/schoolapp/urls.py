from django.urls import path
from . import views
urlpatterns = [
      path('',views.index,name='index'),
      path('form', views.forms, name='form'),
      path('logout',views.logout,name='logout'),
]