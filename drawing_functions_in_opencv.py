import numpy as np
import cv2

#img = cv2.imread('lena.jpg',-1)
img = np.zeros([512,512,3], np.uint8)

img = cv2.line(img, (0,0), (255,255), (255,0,0), 5) 
img = cv2.arrowedLine(img, (0,0), (255,255), (255,0,0), 10) 
img = cv2.rectangle(img, (100,100), (350,350), (0,0,255), 5)
img = cv2.circle(img, (447,63), 63, (0,255,0),-1)   #-1 will fill the circle

font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'OpenCv', (10,500), font, 4, (255,255,255), 5, cv2.LINE_AA)

#img = cv2.polylines(img, (100,100), 0, (255,255,255))

cv2.imshow('lena image', img)

k = cv2.waitKey(0)

cv2.destroyAllWindows()