
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings  
from django.conf.urls.static import static  
from django.contrib.auth import views as auth_view

app_name = 'browsing'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerPage, name='registerPage'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('movies/<int:id>/',views.moviesbooking,name='moviesbooking'),
    path('reserves/<int:id>/', views.reservedetails, name='reservedetails'),
    path('privacy/', views.privacy, name='privacy'),
    path('TermsAndService/', views.terms, name='terms'),
    path('About/', views.about, name='about'),
    path('FAQ/', views.faq, name='faq'),
    path('Services/', views.services, name='services'),
    path('Search/', views.searchBar, name='search'),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  