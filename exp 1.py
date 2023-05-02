import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)

path = "C:/Users/joyce/Pictures/Saved Pictures/Screenshot 2022-12-08 112244.png"
img =  cv2.imread(path)

cv2.imshow("Lena",img)

cv2.waitKey(0)
