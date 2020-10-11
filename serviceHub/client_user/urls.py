from django.urls import path
from . import views


urlpatterns = [
    path('client_home', views.home, name='client_home'),
    path('book-service/<int:pk>', views.book_service, name='book-service'),
    path('raised-sr', views.raised_sr, name='raised-sr')
]