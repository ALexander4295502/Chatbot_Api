from django.views import generic
from django.http.response import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from pprint import pprint
from chatbot.urls import chatBot
import json


# Create your views here
# import required modules
class ChatBotView(generic.View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        # Convert the text payload into a python dictionary
        message = json.loads(self.request.body.decode('utf-8'))
        response = chatBot.get_response(message['content'])
        pprint(message['content'])
        pprint(response.__dict__)
        return JsonResponse({
            'message': response.text
        })

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello World!")
