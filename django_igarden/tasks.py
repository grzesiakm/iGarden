import os
import smtplib
import imghdr
from users.models import Profile
from igarden.models import Flower
from django.core.mail import send_mail
from django.template.loader import render_to_string
from celery2 import task


@task()
def send_reminder():
    subject = "Reminder"
    logged_user = self.request.user
    user_mail = logged_user.email
    message = render_to_string("reminder_email.html", {"user": user, "flower": Flower.name})
    send_mail(subject, message, "marta1317.mg@gmail.com", [user.email], fail_silently = False,)