import cv2
import numpy as np

color_parameters = [
    # h_min s_min v_min h_max s_max v_max
    [90, 86, 40, 133, 178, 79],    # Blue
    [0, 126, 128, 32, 255, 255],   # Yellow
    [33, 98, 81, 69, 255, 255]     # Green
]


def findColors(img, color_parameters):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in color_parameters:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(hsv_img, lower, upper)
        # cv2.imshow(str(color[0]), mask)
        getContours(mask)

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 1000:
            cv2.drawContours(img_copy, cnt, -1, (255, 0, 255), 3)


cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img_copy = img.copy()
    findColors(img, color_parameters)
    cv2.imshow('Result', img_copy)
    cv2.waitKey(1)
