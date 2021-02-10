import cv2
import numpy as np
from canvas import Canvas
from KNN_model import KNN
from point_2d import Point2D

WINDOWS_NAME: str = 'KNN demonstration'
WIDTH: int = 1000
HEIGHT: int = 600

c = Canvas(WIDTH, HEIGHT)
model = KNN(k=3)

def nothing(args):
    pass


def mouseControl(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        c.add_point(x,y,param.color)
        print(f"x: {x} - y: {y}")
        model.dataset.add_point(Point2D(x,y,param.color))
    else:
        pass


def keyboardControl(key):
    if key == ord('q'):
        cv2.destroyAllWindows()
        return False
    return True


class Param:
    def __init__(self):
        self.color = 0
        self.n_neighbour = 0

    def set_color(self,value):
        self.color=value

    def set_n_neighbour(self,value):
        self.n_neighbour = value
        model.k = value


def main():
    p = Param()

    cv2.namedWindow(WINDOWS_NAME)

    cv2.createTrackbar('color', WINDOWS_NAME, 0, 2, p.set_color)
    cv2.createTrackbar('K', WINDOWS_NAME, 1, 20, p.set_n_neighbour)
    cv2.setMouseCallback(WINDOWS_NAME, mouseControl, p)

    main_loop = True
    while main_loop:
        cv2.imshow(WINDOWS_NAME, (np.maximum(c.frame,c.background)))
        key_input = cv2.waitKey(1) & 0xFF
        main_loop = keyboardControl(key_input)
        step = 10
        # print(model.k)
        for x in range(step, WIDTH, step):
            for y in range(0, HEIGHT, step):
                if c.point_counter != 0:
                    point = Point2D(x,y)
                    label = model.find_label_of_a_point(point)
                    c.background[y-step:y+step, x-step:x+step, :] = 0
                    c.background[y-step:y+step, x-step:x+step, label] = 50


if __name__ == '__main__':
    main()