from django.urls import path
from adverts import views


app_name = 'adverts'


urlpatterns = [
    path('create/', views.AdvertCreateView.as_view(), name='create_advert'),
    path('all/', views.AdvertListView.as_view(), name='adverts'),
    path('filters-ad/', views.big_filter_ad, name='filters_advert'),
    path('<slug:slug>/', views.AdvertDetailView.as_view(), name='advert_detail'),
    path('update/<slug:slug>', views.AdvertUpdateView.as_view(), name='advert_update'),
    path('delete/<slug:slug>', views.AdvertDeleteView.as_view(), name='advert_delete'),
    path('del_adv_from_fav', views.del_advert_from_favorites, name='del_fav'),
    path('add_adv_from_fav', views.add_advert_from_favorites, name='add_fav')
]