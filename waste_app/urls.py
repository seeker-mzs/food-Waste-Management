from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('donate_food/', views.donate_food, name='donate_food'),
    path('request_food/', views.request_food, name='request_food'),
    path('track_waste/', views.waste_tracking, name='track_waste'),
    # path('login/', views.login_view, name='login'),  # Login view
    # path('logout/', LogoutView.as_view(), name='logout'),
]
