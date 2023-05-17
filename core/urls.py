from django.urls import path

from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search/<str:keyword>/<int:page>/', views.search, name='search'),
    path('redirect/<path:url>/', views.redirect, name='redirect'),
    path('date/<int:day>-<int:month>-<int:year>/', views.date, name='date'),
    path('article/<int:id>/<slug:title>/', views.article, name='article'),
    path('map/', views.map, name='map'),
]