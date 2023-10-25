from django.urls import path

from teachers import views

urlpatterns = [
    path('',views.Home),
    path('about',views.about),
    path('contact',views.contact),
    path('services',views.services),
]