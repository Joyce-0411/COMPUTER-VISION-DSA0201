kernel = np.array(["[0, -1, 0]",
                  " [-1, 5,-1]",
                   "[0, -1, 0]"])
image_sharp = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
cv2.imshow("C:Usersjoyce/OneDrive/Pictures/316453.jpg", image_sharp)
cv2.waitKey()
cv2.destroyAllWindows()
