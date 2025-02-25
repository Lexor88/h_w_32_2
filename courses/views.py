from django.shortcuts import render

# Create your views here.
import stripe
from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Course
from .stripe_api import create_product, create_price, create_checkout_session

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreatePaymentView(APIView):
    @swagger_auto_schema(
        operation_description="Создание ссылки на оплату курса",
        responses={200: openapi.Response("Ссылка на оплату курса")},
    )
    def get(self, request):
        course = Course.objects.first()
        if not course:
            return Response({"error": "Нет доступных курсов"}, status=400)

        product_id = create_product(course.title, course.description)
        price_id = create_price(product_id, course.price)
        session_url = create_checkout_session(
            price_id,
            success_url="http://127.0.0.1:8000/success/",
            cancel_url="http://127.0.0.1:8000/cancel/"
        )

        return Response({"checkout_url": session_url})
