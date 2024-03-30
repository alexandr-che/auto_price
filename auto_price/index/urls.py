from django.urls import path
#from adverts import views
from index import views


app_name = 'index'


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about')
]