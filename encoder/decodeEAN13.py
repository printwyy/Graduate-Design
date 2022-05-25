import zxing
#识别条形码

def decodeean13(n):
    reader = zxing.BarCodeReader()
    barcode = reader.decode(n)
    answer=barcode.parsed
    print(answer)
    return answer

if __name__ == '__main__':
    m="4.jpg"
    decodeean13(m)