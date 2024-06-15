import base64
from io import BytesIO
import json
import os
from flask import Flask,request,jsonify
from deepface import DeepFace
from PIL import Image
from numpy import asarray

app =Flask(__name__)


@app.route('/')
def main():
    if(request.method=="POST"):
        img1Path=request.json['img1Path']
        img2Base64String=request.json['img2Base64']
        if 'data:image' in img2Base64String:
            img2Base64String=img2Base64String.split(',')[1]
        imgBytes=base64.b64decode(img2Base64String)
        imageStream=BytesIO(imgBytes)
        image=Image.open(imageStream)
        # img1Path='env\IMG_20240612_205619.jpg'
        # image=Image.open('env\IMG_20240612_205627.jpg')  
        imgArray=asarray(image)
        result = DeepFace.verify(img1_path=img1Path,img2_path=imgArray)
    if(request.method=="GET"):
        result={'result':"done"}
    return jsonify(result)
port = int(os.environ.get('PORT', 5000))
if __name__=='__main__':
    app.run(host='0.0.0.0', port=port, debug=True)