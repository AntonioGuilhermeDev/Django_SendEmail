from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.

#Fill in respectively with Subject, message, email origin, recipients.

def enviaemail(request):
    send_mail('',
              '',
                '',
                  ['', ''])
    return HttpResponse('Email enviado!')

from django.shortcuts import render
from django.conf import settings
from .email_utils import send_email_with_attachment


#Attachment upload
 
#Allocate value to respective variables.

def my_email_with_attachment_view(request):
    subject = ''
    message = ''
    from_email = ''
    recipient_list = [''] 
    attachment_path = ''

    file_path = settings.BASE_DIR / attachment_path

    send_email_with_attachment(subject, message, from_email, recipient_list, attachment_path)

    return HttpResponse("Email enviado!")
