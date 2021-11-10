from django.urls import path
from . import views

app_name= 'portfolio'
urlpatterns = [
    # localhost:8000にアクセスしたとき、viewsからindexを読み込んで、nameをindexに
    path('', views.index, name='index'),
    path('works/', views.work, name='works'),

]                                       