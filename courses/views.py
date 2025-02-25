from django.shortcuts import render

# Create your views here.
import stripe
from django.conf import settings
from django.http import JsonResponse
from .models import Course
from .stripe_api import create_product, create_price, create_checkout_session

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_course_payment(request):
    """Создание ссылки на оплату курса"""
    course = Course.objects.first()  # Берём первый курс из базы (для теста)

    if not course:
        return JsonResponse({"error": "Нет доступных курсов"}, status=400)

    product_id = create_product(course.title, course.description)
    price_id = create_price(product_id, course.price)

    session_url = create_checkout_session(
        price_id,
        success_url="http://127.0.0.1:8000/success/",
        cancel_url="http://127.0.0.1:8000/cancel/"
    )

    return JsonResponse({"checkout_url": session_url})