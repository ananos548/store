from django.views.generic import CreateView

from .models import Mailing
from .forms import MailingForm
from .tasks import send_spam_email


class MailingView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing/mailing_form.html'

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        form.save()
        # send(form.instance.email)
        send_spam_email.delay(form.instance.email)  # delay говорит о том, что нужно запускать без ожидания ответа
        return super().form_valid(form)
