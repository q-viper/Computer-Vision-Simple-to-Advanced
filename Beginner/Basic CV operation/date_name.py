import datetime
import cv2

cap=cv2.VideoCapture(0)

#print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

a=int(cap.get(3))
b=int(cap.get(4))
size=(a,b)

result = cv2.VideoWriter('demotimeanddate.avi',
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10,size )
while(True):
    ret,frame=cap.read()
    if ret == True:
        result.write(frame)
        font=cv2.FONT_HERSHEY_COMPLEX
        text="width:" +str(cap.get(3)) + "Heights" + str(cap.get(4))
        datet=str(datetime.datetime.now())
        frame=cv2.putText(frame,datet,(10,50),font,1,(0,255,0),2,cv2.LINE_AA)
        cv2.imshow("img",frame)

        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

