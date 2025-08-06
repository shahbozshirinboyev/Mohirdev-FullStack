from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser
from django.core.mail import send_mail

# @receiver(qaysi_method_ishlaganda, sender=Qaysi_modelni)
@receiver(post_save, sender=CustomUser)
def send_welcome_email(sender, instance, created, **kwargs):
  if created:
    send_mail(
          "Welcome to GoodreadsClone",
          f"Hi, {instance.username}. Welcome to GoodreadsClone. Enjoy the books and reviews.",
          "jrahmonov2@gmail.com",
          [instance.email],
        )