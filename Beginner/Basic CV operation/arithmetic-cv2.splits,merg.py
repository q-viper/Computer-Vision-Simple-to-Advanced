import cv2
img=cv2.imread("H:\CV projects\Basic_CV\images\desktop_w.jpg")
img2=cv2.imread("H:\CV projects\Basic_CV\images\desktop_wall1.png")


print(img.shape)
print(img.size)
print(img.dtype)

b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))

img=cv2.resize(img,(700,710))
img2=cv2.resize(img2,(700,710))


#dst=cv2.add(img2,img)
dst=cv2.addWeighted(img,.9,img2,.1,0)
cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()