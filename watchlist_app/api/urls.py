from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewtList,ReviewDetail


urlpatterns = [
    
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    
    path('stream/', StreamPlatformAV.as_view(), name ='stream-list'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name = 'stream-detail'),
    
    path('review/', ReviewtList.as_view(), name ='review-list'),
    path("review/<int:pk>", ReviewDetail.as_view(), name = 'review-derail')

]
