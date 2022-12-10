from django.urls import path

from ProductApp.views import HomeView, LogoutView,ProductView

urlpatterns=[
    path('',HomeView,name='home'),
    path('product/',ProductView,name='pro'),
    path('logout/',LogoutView,name='log')
]