import base64
from io import BytesIO
import json
from flask import Flask,request,jsonify

app =Flask(__name__)

@app.route('/',methods=['GET'])
def main():
    # img1Path=request.json['img1Path']
    # img2Base64String=request.json['img2Base64']
    # if 'data:image' in img2Base64String:
    #     img2Base64String=img2Base64String.split(',')[1]
    # imgBytes=base64.b64decode(img2Base64String)
    # imageStream=BytesIO(imgBytes)
    # image=Image.open(imageStream)
    # # img1Path='env\IMG_20240612_205619.jpg'
    # # image=Image.open('env\IMG_20240612_205627.jpg')  
    # imgArray=asarray(image)

    # result = DeepFace.verify(img1_path=img1Path,img2_path=imgArray)
    # # print(json.dumps(result,indent=2))
    return jsonify({'result':'done'})

if __name__=='__main__':
    app.run()