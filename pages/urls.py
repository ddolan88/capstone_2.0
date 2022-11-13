from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    Dev1,
    Dev2,
)

urlpatterns=[
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('dev1/', Dev1.as_view(), name='dev1'),
    path('dev2/', Dev2.as_view(), name='dev2'),
]