from django.contrib import admin
from django.urls import path
from web import views
from django.urls import re_path

urlpatterns = [
    path('customer/add/',views.customer_insert),
    path('customer/sel/',views.customer_select),
    path('customer/mod/',views.customer_modify),
    path('customer/del/',views.customer_delete),
    path('administrator/add/',views.administrator_insert),
    path('administrator/sel/',views.administrator_select),
    path('administrator/mod/',views.administrator_modify),
    path('administrator/del/',views.administrator_delete),
    path('court/add/',views.court_insert),
    path('court/sel/',views.court_select),
    path('court/mod/',views.court_modify),
    path('court/del/',views.court_delete),
    path('status/add/',views.status_insert)
]