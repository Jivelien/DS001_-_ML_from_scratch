#!/usr/bin/python3

import numpy as np
import cv2
from model import linear_regression
from dataset import dataset
import canva

WINDOWS_NAME = 'regression'
d = dataset()
c = canva.canva(1400, 800)
lr = linear_regression(theta_lenght=2, learning_rate=1)


def rescale(value, mininit, maxinit, minfinal=0, maxfinal=1):
    scaleinit = maxinit - mininit
    scalefinal = maxfinal - minfinal
    return (value - mininit) / (scaleinit) * scalefinal + minfinal



def on_left_click(x, y):
    c.add_point(x, y)
    d.add_point(rescale(x, 0, c.width, 0, 1), rescale(y, 0, c.height, 1, 0))


def mouseControl(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        on_left_click(x, y)
    else:
        nothing()


def nothing(**args):
    pass


rang = np.arange(0, 1, 1/c.width)
xs = rescale(rang, 0, 1, 0, c.width)

cv2.namedWindow(WINDOWS_NAME)
cv2.setMouseCallback(WINDOWS_NAME, mouseControl)

while True:
    if d.number_of_points >= 2:
        lr.gradient_descent(d.get_x(), d.get_y())

        cc = canva.canva(c.width, c.height, circle_size=1)
        ys = rescale(
                lr.hyp_func(rang, lr.theta), 1, 0, 0, c.height)
        
        for i in range(len(ys)):
            if ys[i] >= 0 and ys[i] < c.width:
                cc.add_point(int(xs[i]), int(ys[i]))
                
        img = cv2.cvtColor(c.canva.astype('uint8'), cv2.COLOR_GRAY2RGB)
        img[:, :, canva.color.RED] = cv2.addWeighted(
            c.canva, 1, cc.canva, 1, 0)
    else:
        img = c.canva

    cv2.imshow(WINDOWS_NAME, img)

    K = cv2.waitKey(1) & 0xFF
    if K == ord('q'):
        cv2.destroyAllWindows()
        break
