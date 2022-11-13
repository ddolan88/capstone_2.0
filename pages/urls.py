from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    Dev1,
    Dev2,
    RTX3060,
    RTX3070,
    RTX3080,
)

urlpatterns=[
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('dev1/', Dev1.as_view(), name='dev1'),
    path('dev2/', Dev2.as_view(), name='dev2'),
    path('rtx3060/', RTX3060.as_view(), name='rtx3060'),
    path('rtx3070/', RTX3070.as_view(), name='rtx3070'),
    path('rtx3080/', RTX3080.as_view(), name='rtx3080'),
]