from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

import requests
import sys
import cv2
import numpy as np
import base64


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

def start_page(request):
    print("Start")
    return render(request, "bd.html")

def bd_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        # Read image
        image = cv2.imdecode(np.fromstring(myfile.read(), np.uint8), cv2.IMREAD_UNCHANGED)

        # In memory
        image_content = cv2.imencode('.jpg', image)[1].tostring()
        encoded_image = base64.encodebytes(image_content)
        to_send = 'data:image/jpg;base64, ' + str(encoded_image, 'utf-8')
        print("Reached ------------------ ")
        return render(request, "bd.html", faceDetected=True, num_faces=0, image_to_show=to_send, init=True)
