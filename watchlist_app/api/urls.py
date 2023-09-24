from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewList ,ReviewDetail, ReviewCreate,StreamPlatfromVS


router= DefaultRouter()
router.register('stream', StreamPlatfromVS, basename='streamplatfrom' )

urlpatterns = [
    
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    
    path("",include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name ='stream-list'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name = 'stream-detail'),
    
    path('stream/<int:pk>/review', ReviewList.as_view(), name = 'stream-detail'),
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name = 'stream-create'),
    path("stream/review/<int:pk>", ReviewDetail.as_view(), name = 'review-derail')
    
        
    # path('review', ReviewList.as_view(), name = 'stream-detail'),
    # path("review/<int:pk>", ReviewDetail.as_view(), name = 'review-derail')



]
