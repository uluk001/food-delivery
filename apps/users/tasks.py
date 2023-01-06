import uuid
from celery import shared_task
from django.utils.timezone import now
import datetime

from apps.users.models import User, EmailVerification

@shared_task
def send_emai_verification(user_id):
    user = User.objects.get(id = user_id)
    expiration = now() + datetime.timedelta(hours=48)
    record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
    record.send_verification_email()