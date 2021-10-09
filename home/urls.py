from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login_page', views.login_page, name='login_page'),
    path('register_form', views.register_form, name='register_form'),
    path('advertisements_page', views.advertisements_page,
         name='advertisements_page'),
    path('user_page', views.user_page, name='user_page'),
    path('logout', views.logout, name='logout')

]
