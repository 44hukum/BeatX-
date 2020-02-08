from django.urls import path
from . import views

urlpatterns=[
    path('songs',views.songs_list,name="songs_list"),
    path('songs/<int:pk>',views.songs_detail,name='songs_detail'),
    path('songs/<int:pagenumber>/<int:size>',views.pagination_rest_test,name='pagination')
]
