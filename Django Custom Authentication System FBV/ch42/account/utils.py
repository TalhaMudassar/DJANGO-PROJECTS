from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import threading

class SendEmailThread(threading.Thread):
    """
    Send email asynchronously so the request returns faster.
    """
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


def send_activation_email(recipient_email, activation_url):
    """
    Sends an HTML + plain-text activation email.
    Template: templates/account/activation_email.html
    Context: activation_url
    """
    subject = "Activate your account on " + settings.SITE_NAME
    from_email = 'no_reply@demomailtrap.com'  # friendly sender (Mailtrap sandbox)
    to_email = [recipient_email]

    html_content = render_to_string('account/activation_email.html', {'activation_url': activation_url})
    text_content = strip_tags(html_content)  # fallback for clients without HTML

    email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    email.attach_alternative(html_content, 'text/html')
    SendEmailThread(email).start()


def send_reset_password_email(recipient_email, reset_url):
    """
    Sends an HTML + plain-text password reset email.
    Template: templates/account/reset_password_email.html
    Context: reset_url
    """
    subject = 'Reset Your Password on ' + settings.SITE_NAME
    from_email = 'no_reply@demomailtrap.co'  # as in your code
    to_email = [recipient_email]

    html_content = render_to_string('account/reset_password_email.html', {'reset_url': reset_url})
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    email.attach_alternative(html_content, "text/html")
    SendEmailThread(email).start()
