# # Create your tasks here
#
# import uuid
# from datetime import timedelta
# from django.utils.timezone import now
# from users.models import EmailVerification, User
# from celery import shared_task
#
#
# @shared_task
# def send_email_verification(user_id):
#     user = User.objects.get(id=user_id)
#     expiration = now() + timedelta(minutes=20)
#     record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration, )
#     record.send_verification_email()