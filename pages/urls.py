from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    Dev1View,
    Dev2View,
)

urlpatterns=[
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('dev1/', Dev1View.as_view(), name='dev1'),
    path('dev2/', Dev2View.as_view(), name='dev2'),
]