import cv2
import numpy as np


img1=np.zeros((250,500,3),np.uint8)
img1=cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2=cv2.imread("H:\CV projects\Basic_CV\images\desktop_wall1.png")


img1=cv2.resize(img1,(250,400))
img2=cv2.resize(img2,(250,400))


#bitAnd=cv2.bitwise_and(img2,img1
bitOr=cv2.bitwise_or(img1,img2)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
#cv2.imshow('bitand',bitAnd)
cv2.imshow('bitOR',bitOr)


cv2.waitKey(0)
cv2.destroyAllWindows()