import requests
#根据条码查询商品信息

#request_url = "https://www.mxnzp.com/api/barcode/goods/details?barcode=----&app_id=---&app_secret=----"
def selectcode(barcode):
    request_url="https://www.mxnzp.com/api/barcode/goods/details"

    app_id='tl0jrqszpcmagsh0'
    app_secret='eEZTek9ZUzFZUG5RU0NQT0QxUkRqQT09'
    request_url=request_url+"?barcode="+barcode+"&app_id="+app_id+"&app_secret="+app_secret

    response=requests.get(request_url)
    if response:
        print (response.json())

if __name__ == '__main__':
    barcode = '6920468012114'
    selectcode(barcode)