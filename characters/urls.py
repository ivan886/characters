from django.contrib import admin
from django.urls import path
from . import views, views_universes
from django.conf.urls import url

app_name = "characters"


urlpatterns = [
    url(r'^test/(?P<string>[\w\-]+)/$',views.test),
    path('', views.list, name="list_characters"),
    path('save', views.save,name="save_characters"),
    path('detail/<int:id>', views.detail,name="detail"),
    path('punto_uno', views.puntoUno),
    path('filter/<int:id>/', views.list_filter, name="filter_charaters"),




]
