from django.conf.urls import url
from .views import add_remove_favourites ,view_fav, favourite_list
urlpatterns = [
    url(r'^$', view_fav, name='view_fav'),
    url(r'^addremove/(?P<id>\d+)$', add_remove_favourites, name='add_remove_favourites'),
    url(r'^favourites/(?P<id>\d+)', favourite_list, name='favourite_list'),
]