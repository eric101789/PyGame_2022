from pathlib import Path
import cv2

vc = cv2.VideoCapture('explosion.mp4')
c = 1

if vc.isOpened():
    val, frame = vc.read()
else:
    val = False

timeF = 1000

while val:
    val, frame = vc.read()
    if c % timeF == 0:
        cv2.imwrite('image_'+str(c) + '.jpg', frame)
    c = c + 1
    cv2.waitKey(1)
vc.release()
