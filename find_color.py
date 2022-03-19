import cv2

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2.imshow("Image", img)
    cv2.imshow("HSV", hsv_img)
    cv2.waitKey(1)