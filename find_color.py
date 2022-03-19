import cv2
import numpy as np


def empty(a):
    pass


# TrackBars
cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640, 200)
cv2.createTrackbar('Hue Min', 'TrackBars', 0, 179, empty)
cv2.createTrackbar('Hue Max', 'TrackBars', 179, 179, empty)
cv2.createTrackbar('Sat Min', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('Sat Max', 'TrackBars', 255, 255, empty)
cv2.createTrackbar('Val Min', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('Val Max', 'TrackBars', 255, 255, empty)

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Track Bar Values
    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBars')
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBars')
    s_min = cv2.getTrackbarPos('Sat Min', 'TrackBars')
    s_max = cv2.getTrackbarPos('Sat Max', 'TrackBars')
    v_min = cv2.getTrackbarPos('Val Min', 'TrackBars')
    v_max = cv2.getTrackbarPos('Val Max', 'TrackBars')

    # Mask
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(hsv_img, lower, upper)

    cv2.imshow("Image", img)
    cv2.imshow("HSV", hsv_img)
    cv2.imshow("Mask", mask)
    cv2.waitKey(1)
