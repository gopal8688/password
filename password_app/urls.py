from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('log_in/', views.log_in, name='log_in'),
    path('forget_password/', views.forget_password, name='forget_password'),
    path('new_password/', views.new_password, name='new_password'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('Search/', views.Search, name='Search'),
    path('contact_details/', views.contact_details, name='contact_details'),
    path('Register/', views.Register, name='Register'),
    path('about_project/', views.about_project, name='about_project'),

    # path('admin/', admin.site.urls),
]
