from django.urls import path

from chat.views import HomeView, MessageView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("message/", MessageView.as_view(), name="message"),
]
