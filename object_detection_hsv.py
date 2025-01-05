import numpy as np
import cv2 

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('tracking')
cv2.createTrackbar("LH", "tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "tracking", 255, 255, nothing)
cv2.createTrackbar("US", "tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "tracking", 255, 255, nothing)

while True:
    #frame = cv2.imread('smarties.png')
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h=cv2.getTrackbarPos("LH", "tracking")
    l_S=cv2.getTrackbarPos("LS", "tracking")
    l_V=cv2.getTrackbarPos("LV", "tracking")

    U_h=cv2.getTrackbarPos("UH", "tracking")
    U_S=cv2.getTrackbarPos("US", "tracking")
    U_V=cv2.getTrackbarPos("UV", "tracking")
    
    l_b = np.array([l_h, l_S, l_V])
    u_b = np.array([U_h, U_S, U_V])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()    