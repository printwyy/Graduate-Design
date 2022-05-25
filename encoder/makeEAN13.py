from pystrich.ean13 import EAN13Encoder

def encodeean13(n):
    encoder = EAN13Encoder(n)
    name=n+".jpg"
    encoder.save('./code/'+name)

if __name__ == '__main__':
    m="5602342136215"
    encodeean13(m)