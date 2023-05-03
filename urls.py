from django.urls import include, path
from copydata_app import views

from .views import test
from .views import (
    DataListApiView,
    ImageViewSet,
)

urlpatterns = [
    #path(r'test/', views.test, name='test'),
    path('test/', test.as_view(),name='test_view'),
    path('api/<int:revision>', DataListApiView.as_view()),
    path('api/upload/', views.ImageViewSet.as_view(), name='upload'),
    ]