from django.conf.urls import include, url
from chatbot.settings import SECRET_TOKEN
from .views import ChatBotView

urlpatterns = [
    url(r"^%s/?$" % SECRET_TOKEN, ChatBotView.as_view())
]