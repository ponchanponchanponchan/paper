
import cv2
import numpy as np

img=cv2.imread('/home/fr20e/tm_ws/python/mensaki/hojyonomi.jpg')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imwrite("gray.png", gray)


gray2 = cv2.bitwise_not(gray)
#cv2.imwrite("grayhanten.png", gray2)


im_edges = cv2.Canny(gray2, 130, 285, L2gradient=True)
cv2.imwrite("im_edges.png", im_edges)




"""
#lines = cv2.HoughLinesP(gray2, rho=1, theta=np.pi/360, threshold=80, minLineLength=80, maxLineGap=5)
#lines = cv2.HoughLinesP(gray2, rho=1, theta=np.pi/360, threshold=60, minLineLength=10, maxLineGap=10)
#lines = cv2.HoughLinesP(gray2, rho=1, theta=np.pi/360, threshold=80, minLineLength=30, maxLineGap=5)



for line in lines:
    x1, y1, x2, y2 = line[0]

    
    red_line_img = cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 3)
    cv2.imwrite("calendar_mod3.png", red_line_img)
"""



