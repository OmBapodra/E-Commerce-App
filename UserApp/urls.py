from django.urls import path

from UserApp.views import LoginView,SignupView

urlpatterns=[
    path('',LoginView,name='login'),
    path('signup/',SignupView,name='signup')
]