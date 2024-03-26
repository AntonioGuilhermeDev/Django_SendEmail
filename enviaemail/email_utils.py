import magic
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMessage
import os
from enviaemail import views

def send_email_with_attachment(subject, message, from_email, recipient_list, attachment_path):
    with open(attachment_path, 'rb') as file:
        file_content = file.read()
    mime_type = magic.from_buffer(file_content, mime=True)
    file_name = os.path.basename(attachment_path)
    email = EmailMessage(subject, message, from_email, recipient_list)
    email.attach(file_name, file_content, mime_type)
    email.send()