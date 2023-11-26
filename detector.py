import os, shutil
from flask import Flask, request
from yolov5 import detect as Detect
import base64
import json


prev_id = ''
app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect_target():
    
    # fn_list = request.json['filename']
    # filename = fn_list[0]
    
    # img_list = request.json['image']
    # image_bin = base64.b64decode(img_list[0])
    # fpath = '/home/ubuntu/yolov5/'+ filename
    # with open(fpath, 'wb') as f:
    #     f.write(image_bin)
        
    #get Data
    
    image = request.files['image']
    filename = image.filename
    print(filename)
    fpath = filename
    image.save(fpath)
    # global prev_id
    # file_name = request.form.get('img_path')
    # uuid = request.form.get('uuid')
    # print(file_name)
    ret_path = 'yolov5/runs/detect/woori/'

    if os.path.isdir(ret_path):
        shutil.rmtree(ret_path)
    Detect.detect(fpath, True, True, 'woori')
    
    #Get class folder name
    class_path = ret_path + 'crops/' 
    class_list = os.listdir(class_path)
    image_dict = {}
    
    ret_file =  open(ret_path +'ret_' +filename, 'rb' )
    image_binary = ret_file.read()
    encoded_string = base64.b64encode(image_binary)
    ret_file.close()
    
    image_dict[filename] = encoded_string.decode()
    
    for c in class_list:
        print(c)
        cloth_path = class_path + c
        cloth_list = os.listdir(cloth_path)
        for item in cloth_list:
            item_path = cloth_path + '/'+item
            item_image =  open(item_path, 'rb' )
            item_binary = item_image.read()
            encoded_item = base64.b64encode(item_binary)
            item_image.close()
            key = c+'_'+item
            image_dict[key] = encoded_item.decode()
            
    
    # ret_file =  open(ret_path + filename, 'rb' )
    # image_binary = ret_file.read()
    # encoded_string = base64.b64encode(image_binary)
    # ret_file.close()

    # image_dict = {
    #     'file_name':filename,
    #     filename: encoded_string.decode()
    # }

    image_json = json.dumps(image_dict)

    print(image_json)
    # prev_id = uuid
    return image_json

if __name__ == '__main__':
    app.run(host='0.0.0.0')
