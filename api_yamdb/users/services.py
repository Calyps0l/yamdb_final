from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail


def send_code(user):
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        'Код подтверждения для регистрации на сайте YaMDB',
        f'Ваш код подтверждения: {confirmation_code}',
        'admin@yamdb.com',
        [user.email],
        fail_silently=False,
    )
