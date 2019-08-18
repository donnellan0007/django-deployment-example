from django.urls import path, include
from . import views
from learning_users import urls

app_name = 'basicapp'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('userlogin/',views.user_login,name='login'),
    path('profile/',views.profile_page,name='profile'),
]
