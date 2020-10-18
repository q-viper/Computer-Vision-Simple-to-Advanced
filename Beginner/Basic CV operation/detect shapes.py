import cv2
import numpy

img=cv2.imread('images/bunchofshapes.jpg')
imggrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



cv2.imshow('shapess',img)

cv2.waitKey(0)
cv2.destroyAllWindows()