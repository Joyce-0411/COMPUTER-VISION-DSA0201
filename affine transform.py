import cv2
import numpy as np


img = cv2.imread("C:/Users/joyce/OneDrive/Pictures/316453.jpg")

rows,cols,_ = img.shape


pts1 = np.float32([[50,500],[20,500],[100,50]])


pts2 = np.float32([[10,100],[20,500],[100,30]])


M = cv2.getAffineTransform(pts1,pts2)


dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow("Affine Transform", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
