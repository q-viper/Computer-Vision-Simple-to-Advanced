import cv2
import numpy as np
img=np.zeros([512,512,3],np.uint8)

#img=cv2.imread("images/obama.jpg",1)


img=cv2.line(img,(0,0),(255,255),(0,255,0),5)
img=cv2.arrowedLine(img,(0,255),(255,255),(255,255,0),5)
img=cv2.rectangle(img,(200,0),(510,128),(0,25,230),1)
img=cv2.circle(img,(447,63),63,(0,23,130),-1)

font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img,"opencvdemo",(10,500),font,4,(255,0,30),5,cv2.LINE_AA)

cv2.imshow("cofee",img)

k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
