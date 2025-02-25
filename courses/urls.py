from django.urls import path
from .views import create_course_payment

urlpatterns = [
    path("create-payment/", create_course_payment, name="create-payment"),
]