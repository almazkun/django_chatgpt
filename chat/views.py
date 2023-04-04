from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from chat.forms import MessageForm
from chat.openai_chat import get_response


# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"


class MessageView(FormView):
    template_name = "message.html"
    form_class = MessageForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        message = form.cleaned_data["message"]
        response = get_response(message)
        messages.success(self.request, response)
        return super().form_valid(form)
