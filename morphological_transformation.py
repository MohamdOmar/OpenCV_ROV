import cv2
import numpy as np
from matplotlib import pyplot as plt 


img = cv2.imread('landmine.JPG',cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 210, 255, cv2.THRESH_BINARY)
kernal = np.ones((3,3), np.uint8)
dilation = cv2.dilate(mask, kernal, iterations = 2)

erosion = cv2.erode(mask, kernal, iterations =2)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN , kernal)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE , kernal)

titles = ['a', ' b', 'c', 'd', 'f']  # 'opening','closing']
images = [img , mask, dilation ,erosion ,opening] #, closing]

for i in range(5) :
    plt.subplot(3,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()    