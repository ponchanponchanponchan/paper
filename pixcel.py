import cv2
import numpy as np

threshold=127

im = cv2.imread('/home/fr20e/tm_ws/python/mensaki/2.40_2_1.png', cv2.IMREAD_GRAYSCALE)
whitePixels = cv2.countNonZero(im)

shape = im.shape
size = im.size


print(shape)
print(size)
print(whitePixels)

cv2.imshow("binary",im)
cv2.waitKey(0)
cv2.destroyAllWindows()




