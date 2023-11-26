import requests
import base64

# img_path should be a file_name without path since docker have a different path
#분석할 이미지 파일명
image_url = 'C:/AI/test.jpg'
#분석 작업할 폴더명
UUID ='uri_01'


#이미지파일를 바이트형식으로 변환
with open(image_url, 'rb') as img:
    image_data = base64.b64encode(img.read())

#post방식으로 지정된 주소에 이미지 파일명, 작업폴더명, 이미지바이트형식을 전달
ret = requests.post("http://127.0.0.1:5000/detect", data = {'img_path': image_url, 'uuid':UUID, 'data':image_data})
#ret = requests.post("http://127.0.0.1:5000/detect", data = {'img_path': image_url, 'uuid':UUID})
#ret = requests.post("http://43.200.169.239:5000/detect", data = {'img_path': image_url, 'uuid':UUID, 'data':image_data})
print(ret)