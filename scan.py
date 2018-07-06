from pyzbar import pyzbar
import argparse
import cv2
from pylibdmtx.pylibdmtx import decode
from PIL import Image
import os



def CodeReader(imname):

    print('@@@@@@@@@@@@@@@@')
    image = cv2.imread(imname)

    barcodestemp = decode(image)

    if len(barcodestemp)== 0:
        # find the barcodes in the image and decode each of the barcodes
        barcodes = pyzbar.decode(image)
        model = 'QRCODE'
        print (model)

    else:
        barcodes = barcodestemp
        model = 'DATAMATRIX'
        print (model)


    for barcode in barcodes:

        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # if model == 'QRCODE':
        #     barcodeData = barcode.data.decode("utf-8")
        #     print(barcodeData)
        text = "{} ".format(barcode.data)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 0, 255), 2)

        print(barcode.data.decode(encoding="GB2312", errors="strict"))#UTF-8 不能编码部分中文字符，会提示超出utf-8范围

    print('#'*10)


    cv2.imshow(imname, image)
    cv2.waitKey(200)

if __name__ == '__main__':

    print('Enter the absolute directory of codes:')
    rootdir = input()
    print('directory:', rootdir)

    for filenames in os.walk(rootdir):

        for filename in filenames[2]:
            imname = os.path.join(rootdir, filename)
            print ('Imagename:',imname)
            CodeReader(imname)

