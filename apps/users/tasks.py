import datetime
import uuid

from celery import shared_task
from django.utils.timezone import now

from apps.users.models import EmailVerification, User


@shared_task
def send_emai_verification(user_id):
    user = User.objects.get(id=user_id)
    expiration = now() + datetime.timedelta(hours=48)
    record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
    record.send_verification_email()
