import requests
import base64




request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/qrcode"
# 二进制方式打开图片文件
f = open('3.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '24.0c5a4b55b63b695d2dbb5c6facbec27a.2592000.1650088666.282335-25782062'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())

