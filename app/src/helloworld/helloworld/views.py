from django.http import HttpResponse, JsonResponse
import json
import requests
from random import randint
import pdb
from helloworld import settings
from twilio.twiml.voice_response import Play, VoiceResponse
from twilio.rest import Client


def index(request):
    return HttpResponse("Hello Hasura World!")

def recieve_call(request):

    print(request)
    fileext = randint(0,10)
    file_name = "_question"+str(fileext)
    f = open('myfile.txt', 'w')
    f.write(str(fileext))  # python will convert \n to os.linesep
    f.close()
    response = "<?xml version='1.0' encoding='UTF-8'?>"\
                "<Response>"\
                  "<playtext speed='4' quality='best' >Thank you for calling Voura. We are always here to help you </playtext>"\
                  "<playtext speed='4' quality='best'> Hey friend! Leave your question for us we will get back to you soon </playtext>"\
                   "<record format='wav' silence='3' maxduration='40' >current_user"+file_name+"</record>"\
                  "</Response>"
    return HttpResponse(response)

def speech_to_text():
  return "a"

def text_to_speech():
  return "a"

def find_answer():
  return "a"

def call_to_answer(request):
  account_sid ="AC65f13cfe74133243c85da04c637c0155"
  auth_token = "1755aba669b58f1c865842c0110e1b36"
  client = Client(account_sid, auth_token)
  call = client.calls.create(to="+919860328030",from_="9472825539",url="http://voura.calves93.hasura-app.io/getanswer/")
  return HttpResponse("")

def get_answer(request):
  # response = VoiceResponse()
  # response.play('https://api.twilio.com/cowbell.mp3', loop=10)
  response = "<?xml version='1.0' encoding='UTF-8'?>"\
                "<Response>"\
                 "<Play>https://api.twilio.com/cowbell.mp3</Play>"\
             "</Response>"
  return HttpResponse(response)

def get_question(request):
  f = open('myfile.txt','r')
  fileext = str(f.read())
  response ="<html>"\
              "<body>"\
                "<audio controls>"\
                  "<source src='http://recordings.kookoo.in/voura/current_user_question"+fileext+".mp3' type='audio/mpeg'>"\
                  "Your browser does not support the audio element."\
                "</audio>"\
              "</body>"\
          "</html>"
 # response = "<html><audio><source='http://recordings.kookoo.in/voura/current_user_question0.mp3' type='audio/mpeg'></audio></html>"
  return HttpResponse(response)

# import speech_recognition as yo
# r=yo.Recognizer()
# with yo.WavFile("/home/amura/Downloads/test.wav") as x:
#      au=r.record(x)
# r.recognize_google(au)
