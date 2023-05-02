#image rotation for 180
import cv2


path = r"C:/Users/joyce/Pictures/Saved Pictures/Screenshot 2022-12-08 112244.png"


src = cv2.imread(path)


window_name = 'Image'


image = cv2.rotate(src, cv2.ROTATE_180)


cv2.imshow(window_name, image)
cv2.waitKey(0)
