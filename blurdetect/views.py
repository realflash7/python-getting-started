from django.shortcuts import render
from django.http import HttpResponse

import requests
import sys

from subprocess import run,PIPE

import blurdetect.blur_detection.detection
from blurdetect.process import do_detection

def detect(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "detect.html")

def output(request):
    data='Fdgdf'
    print(data)
    data=data
    out='out---------------put'  
    out2=do_detection('hazy.png', 'results.json')
    print(out2)
    print(out)
    return render(request,'detect.html',{'data':out2})

