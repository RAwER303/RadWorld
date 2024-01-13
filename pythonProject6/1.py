import time
import cv2 as cv
import cv2
from playsound import playsound
image = cv2.imread('rtr.png')
img = cv2.imread('svchk.png')
im = cv2.imread('chep1.png')
iq = cv2.imread('pferd.png')
a="indus"
b="savchk"
c="chepchik"
i=0
while True:
    a= a+str(i)
    i=i+1
    cv2.imshow(a, image)
    cv2.imshow(b, img)
    cv2.imshow(c, im)
    cv2.imshow(c, iq)
    cv.waitKey(27)
    time.sleep(0.1)
    b= b+str(i)
    i=i+1
    c = c + str(i)
