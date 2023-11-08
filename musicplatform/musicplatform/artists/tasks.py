from .models import Artist
from celery import shared_task
from django.core.mail import send_mail
from musicplatform.settings import EMAIL_HOST_USER
from datetime import timedelta, datetime


@shared_task(bind=True)
def send_inactivity_reminder_emails(self):
    thirty_days_ago = datetime.now() - timedelta(days=30)
    artists = Artist.objects.filter(
        albums__release_datetime__lte=thirty_days_ago).distinct()
    for artist in artists:
        user = artist.user
        mail_subject = "Don't Let Your Popularity Decrease!"
        message = "It has been 30 days since you created an album.\nKeep your fans engaged by creating new music on our platform."
        to_email = user.email
        from_email = EMAIL_HOST_USER

        send_mail(subject=mail_subject, message=message, from_email=EMAIL_HOST_USER,
                  recipient_list=[to_email], fail_silently=False)

   # return "Done"
