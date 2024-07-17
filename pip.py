
	
import cv2
import numpy as np
 
def calc_black_whiteArea(bw_image):
    image_size = bw_image.size

    whitePixels = cv2.countNonZero(bw_image)
    blackPixels = bw_image.size - whitePixels
 
    whiteAreaRatio = (whitePixels*100/float(image_size))
    blackAreaRatio = (blackPixels*100/float(image_size))
    



    h, w = bw_image.shape
    size = bw_image.size


    print('width: ', w)
    print('height:', h)
    print(size)







    print("White Area [%] : ", whiteAreaRatio)
    print("Black Area [%] : ", blackAreaRatio)
    
    print(blackPixels)
    print(whitePixels)
    print(image_size)







 
if __name__ == "__main__":
    # read input image
    image = cv2.imread('/home/fr20e/tm_ws/python/mensaki/2.40_2(1).png')
 
    # convert grayscale image
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
 
    # black white
    ret, bw_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_OTSU)
 
    # save image
    cv2.imwrite("blackwhite2.40_2(1).jpg", bw_image)
 
    # calculation black and white area
    calc_black_whiteArea(bw_image)