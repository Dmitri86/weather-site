from django.urls import path, re_path
from . import views

urlpatterns = [
    path('answer/<str:city>', views.answer, name='answer_url'),
    path('', views.index, name='index'),
    path('answer', views.enter, name="enter_city_url")
]