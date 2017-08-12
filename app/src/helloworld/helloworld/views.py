from django.http import HttpResponse, JsonResponse
import json
import requests
from random import randint
import pdb
from helloworld import settings


def index(request):
    return HttpResponse("Hello Hasura World!")

def recieve_call(request):
    print(request)
    fileext = randint(0,10)
    pdb.set_trace()
    response = "<?xml version='1.0' encoding='UTF-8'?>"\
                "<Response>"\
                  "<playtext speed='4' quality='best' >Thank you for calling Voura. We are always here to help you </playtext>"\
                  "<playtext speed='4' quality='best'> Hey friend! Leave your question for us we will get back to you soon </playtext>"\
                   "<record format='wav' silence='3' maxduration='40' >current_user_" +str(fileext)+ "</record>"\
                  "</Response>"
    return HttpResponse(response)

