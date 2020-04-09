from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('<h1>CV-WASTELAND /ᐠ｡‸｡ᐟ\ﾉ</h1>')