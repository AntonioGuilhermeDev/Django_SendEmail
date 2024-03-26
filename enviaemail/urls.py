from django.urls import path
from enviaemail import views 

urlpatterns = [
    path('email/', views.my_email_with_attachment_view, name='envia_email'),
]