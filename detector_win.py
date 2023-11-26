#플라스크 서버 구동
import os, shutil
from flask import Flask, request
from yolov5 import detect as Detect
import base64


prev_id = ''
app = Flask(__name__)

#맵핑명 /일 경우 접속 메소드
@app.route('/')
def home():
   return 'This is Home!'

#맵핑명 /detect, POST 방식인 경우 접속 메소드
@app.route('/detect', methods=['POST'])
def detect_target():
    global prev_id

    #img_path로 전달받은 값을 file_name에 저장(이미지파일명)
    file_name = request.form.get('img_path')
    #data로 전달받은 값을 img에 저장(이미지 바이트형식)
    img = request.form.get('data')
    ret_img_string = img
   #이미지데이터를 바이트형으로 변환해서 플라스크 서버에 test.jpg로 복사
    img = base64.b64decode(ret_img_string)
    file = open("test.jpg", 'bw')
    file.write(img)
    file.close()
    
   #uuid로 전달받은 값을 uuid에 저장(폴더명)
    uuid = request.form.get('uuid')
    print(file_name)

   #이미지 추론
    #shutil.rmtree('/AI/yolov5/runs/detect/')
    Detect.detect("./test.jpg", True, True, uuid)
    prev_id = uuid
    return 'Hello Flask World'

#플라스크 서버 접속 주소
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
