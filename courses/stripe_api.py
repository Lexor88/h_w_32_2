import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY  # Устанавливаем API-ключ

def create_product(name, description):
    """Создание продукта в Stripe"""
    try:
        product = stripe.Product.create(name=name, description=description)
        return product.id
    except stripe.error.StripeError as e:
        return f"Ошибка при создании продукта: {e.user_message}"

def create_price(product_id, amount):
    """Создание цены для продукта"""
    try:
        price = stripe.Price.create(
            unit_amount=int(amount * 100),  # Цена в центах
            currency="usd",
            product=product_id,
        )
        return price.id
    except stripe.error.StripeError as e:
        return f"Ошибка при создании цены: {e.user_message}"

def create_checkout_session(price_id, success_url, cancel_url):
    """Создание сессии оплаты"""
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{"price": price_id, "quantity": 1}],
            mode="payment",
            success_url=success_url,
            cancel_url=cancel_url,
        )
        return session.url
    except stripe.error.StripeError as e:
        return f"Ошибка при создании сессии: {e.user_message}"
