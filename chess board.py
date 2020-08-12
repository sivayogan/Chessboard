import numpy as np
import cv2
b=np.ones([400,400],dtype="uint8")
for i in range(50,401,100):
	for j in range(50,401,100):
		b[i:i+50,j:j+50]=255
for i in range(0,401,100):
	for j in range(0,401,100):
		b[i:i+50,j:j+50]=255
cv2.imshow("chessboard",b)
cv2.waitKey()