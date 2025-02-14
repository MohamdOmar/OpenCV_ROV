import numpy as np
import cv2 as cv

def nothing(x):
    print(x)

#create a black image, a window
cv.namedWindow('image')

cv.createTrackbar("CP", 'image', 10, 400, nothing)

switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    img = cv.imread('lena.jpg')
    pos = cv.getTrackbarPos('CP', 'image')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (50,150), font, 6, (0,0,255), 10)

    k = cv.waitKey(1) & 0xFF
    if 27 == k:
        break
    
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        
    img= cv.imshow('image',img)
        

cv.destroyAllWindows() 