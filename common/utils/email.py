from django.core.mail import EmailMessage


def send_email(to, subject, content, sender='admin@example.com'):
    email = EmailMessage(
        subject=subject,
        body=content,
        from_email=sender,
        to=[to],
    )
    email.content_subtype = 'html'
    return email.send()