from pyzbar import pyzbar
import argparse
import cv2
from pylibdmtx.pylibdmtx import decode
from PIL import Image
import os



def CodeReader(imname):

    print('test on:',imname)
    image = cv2.imread(imname)

    barcodestemp = decode(image)

    if len(barcodestemp)== 0:
        # find the barcodes in the image and decode each of the barcodes
        barcodes = pyzbar.decode(image)
        model = 'QRCODE'

    else:
        barcodes = barcodestemp
        model = 'DATAMATRIX'



    for barcode in barcodes:

        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        info = barcode.data.decode(encoding="GBK", errors="strict")
        text = "[Type]: {} \n[Info]: {} ".format(model,info)#UTF-8 不能编码部分中文字符，会提示超出utf-8范围,所以用GBK
        cv2.putText(image, info, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 0, 255), 2)
        print(text)
    print('\n')

    cv2.imshow('Barcode', image)
    cv2.waitKey(0)

if __name__ == '__main__':

    print('Enter the absolute directory of codes:')
    rootdir = input()
    print('code directory:', rootdir)
    print ('start codereader....')

    for filenames in os.walk(rootdir):

        for filename in filenames[2]:
            imname = os.path.join(rootdir, filename)

            CodeReader(imname)

