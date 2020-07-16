import cv2
import numpy as nm
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    success,img = cap.read()
    code = decode(img)
    for qrCode in code:
        text =qrCode.data.decode('utf-8')
        points = nm.array([qrCode.polygon],nm.int32)
        cv2.polylines(img, [points], True, (0,255,0), 3)
        print(text)
    cv2.imshow('Result', img)
    cv2.waitKey(2)