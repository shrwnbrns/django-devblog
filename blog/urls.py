from django.urls import path
from .views import post_list_view, post_create_view, signup_view, login_view, logout_view

urlpatterns = [
    path('', post_list_view, name='post_list'),
    path('create/', post_create_view, name='post_create'),
    path('singup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout', logout_view, name='logout'),

]