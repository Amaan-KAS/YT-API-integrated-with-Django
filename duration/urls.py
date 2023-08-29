from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='duration-home'),
    path('about/', views.about, name='duration-about'),
    path('user_info/', views.user_info_view, name='user_info_view')

    # path('about/', views.about, name='duration-about'),
]