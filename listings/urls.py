from django.urls import path
from .views import *
urlpatterns = [
    path("booking/",BookingInfoView.as_view()),
    path("booking/<int:price>",BookingInfoView.as_view()),
]


# Execute URL : 127.0.0.1:8000/booking/70?price=lessthan
