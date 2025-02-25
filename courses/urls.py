from django.urls import path
from .views import CreatePaymentView  # Импортируем классовое представление

urlpatterns = [
    path("create-payment/", CreatePaymentView.as_view(), name="create-payment"),  # Используем .as_view()
]