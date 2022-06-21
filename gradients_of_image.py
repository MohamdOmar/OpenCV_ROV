import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('sudoku.png',cv2.IMREAD_GRAYSCALE)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

soblX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
soblY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
edges = cv2.Canny(img, 100, 200)

soblX = np.uint8(np.absolute(soblX))
soblY = np.uint8(np.absolute(soblY))

sobelcombined = cv2.bitwise_or(soblX,soblY)

titles = ['image', 'laplacian', 'soblX', 'soblY','sobelcombined','edges']
images = [img, lap, soblX, soblY, sobelcombined, edges]


for i in range(6):
    plt.subplot(3,3,i+1) , plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks()

plt.show()