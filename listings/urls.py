from django.urls import path
from .views import *
urlpatterns = [
    path("booking/",BookingInfoView.as_view()),
    path("booking/<int:price>",BookingInfoView.as_view()),
]
