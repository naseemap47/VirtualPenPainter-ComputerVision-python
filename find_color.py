import cv2


def empty(a):
    pass


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

    cv2.imshow("Image", img)
    cv2.imshow("HSV", hsv_img)
    cv2.waitKey(1)
