import os
import smtplib
import imghdr
from email.message import EmailMessage
from celery2.decorators import periodic_tasks
from celery2.task.schedules import crontab


@periodic_tasks(name="send")
def send():
    EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    msg = EmailMessage()
    msg['Subject'] = 'Water Reminder'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'mrtgrzesiak@gmail.com'

    msg.set_content('This is a plain text email')

    msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:SlateGray;">This is an HTML Email!</h1>
        </body>
    </html>
    """, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        