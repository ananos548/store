from django.core.mail import send_mail


def send(email):
    send_mail(
        'You was subscribe on the mailing',  # subject
        'Thank you',    # message
        'vapmaksim6@gmail.com',   # from_email
        [email],
        fail_silently=False,
    )
