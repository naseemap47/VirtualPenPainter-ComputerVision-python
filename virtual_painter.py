import cv2
import numpy as np

color_parameters = [
    # h_min s_min v_min h_max s_max v_max
    [90, 86, 40, 133, 178, 79],  # Blue
    [0, 126, 128, 32, 255, 255],  # Yellow
    [33, 98, 81, 69, 255, 255]  # Green
]
color_value = [
    # BGR Format
    [255, 0, 0],  # Blue
    [0, 255, 255],  # Yellow
    [0, 255, 0]  # Green
]

draw_position = []


def findColors(img, color_parameters, color_value):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    for color in color_parameters:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(hsv_img, lower, upper)
        # cv2.imshow(str(color[0]), mask)
        x, y = getContours(mask)
        cv2.circle(img_copy, (x, y), 5, color_value[count], cv2.FILLED)
        if x != 0 and y != 0:
            draw_position.append([x, y, count])
        count += 1


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 1000:
            cv2.drawContours(img_copy, cnt, -1, (255, 0, 255), 3)
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + (w // 2), y


def drawPen(img, positions, color_val):
    for position in positions:
        print(position)
        cv2.circle(img, (position[0], position[1]),
                   5, color_val[position[2]], cv2.FILLED
                   )


cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img_copy = img.copy()
    findColors(img, color_parameters, color_value)
    # print(draw_position)
    drawPen(img, draw_position, color_value)
    cv2.imshow('Result', img_copy)
    cv2.waitKey(1)
