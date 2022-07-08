from urllib.parse import urlparse
from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('site/', views.SiteView.as_view(), name='site'),
    path('NewsView/', views.NewsView.as_view(), name='NewsView'),
    path('TatemonoView/', views.TatemonoView.as_view(), name='TatemonoView'),
    path('NotatemonoView/', views.NotatemonoView.as_view(), name='NotatemonoView'),
    path('KokuhouView/', views.KokuhouView.as_view(), name='KokuhouView'),
    path('list/', views.ListView.lists, name='lists'),
    path('list/<int:pk>/', views.ListView.detail, name='detail'),

]