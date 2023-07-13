from django.urls import path
from MyDjangoApp import views
from django.views.generic import TemplateView
urlpatterns = [
    path('add_book/', views.add_book),
    path('show_books/', views.show_books),
]
