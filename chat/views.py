from typing import List

from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView

from chat import cacher
from chat.forms import MessageForm
from chat.providers.open_ai import get_response

DEFAULT_CONVERSATION = [
    {
        "role": "system",
        "content": "Welcome to the chatbot! Ask anything!",
    },
    {
        "role": "user",
        "content": "Hello!",
    },
    {
        "role": "assistant",
        "content": "Hello, how are you?",
    },
    {
        "role": "user",
        "content": "I'm good, how are you?",
    },
    {
        "role": "assistant",
        "content": "I'm good, thanks for asking.",
    },
    {
        "role": "system",
        "content": "Conversation ended.",
    },
]


class HomeView(FormView):
    template_name = "home.html"
    form_class = MessageForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        conversation = cacher.get("conversation") or DEFAULT_CONVERSATION
        conversation.append({"role": "user", "content": form.cleaned_data["message"]})
        cacher.set("conversation", get_response(conversation))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["conversation"] = cacher.get("conversation") or DEFAULT_CONVERSATION
        return context

    def get_template_names(self) -> List[str]:
        if self.request.htmx:
            return ["partial/home.html"]
        return super().get_template_names()


class ResetCacheView(RedirectView):
    url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        cacher.clear()
        return super().get(request, *args, **kwargs)
