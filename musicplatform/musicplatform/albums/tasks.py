from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from musicplatform.settings import EMAIL_HOST_USER


@shared_task(bind=True)
def send_congrats_mail(self, artist, album):
    user = artist.user
    mail_subject = "Music Platform"
    message = f"Congratulations for releasing your new album{album.name}"
    to_email = user.email
    send_mail(subject=mail_subject, message=message, from_email=EMAIL_HOST_USER,
              recipient_list=[to_email], fail_silently=False)

    return "Done"
