import cv2
from canvas import Canvas

WINDOWS_NAME: str = 'KNN demonstration'
WIDTH: int = 1000
HEIGHT: int = 600

c = Canvas(WIDTH, HEIGHT)


def nothing(args):
    pass


def mouseControl(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        c.add_point(x,y,param.color)
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
        self.n_neighbour=value


def main():
    p = Param()
    cv2.namedWindow(WINDOWS_NAME)

    cv2.createTrackbar('color', WINDOWS_NAME, 0, 2, p.set_color)
    cv2.createTrackbar('N', WINDOWS_NAME, 0, 20, p.set_n_neighbour)
    cv2.setMouseCallback(WINDOWS_NAME, mouseControl, p)

    main_loop = True
    while main_loop:
        cv2.imshow(WINDOWS_NAME, c.frame)
        key_input = cv2.waitKey(1) & 0xFF
        main_loop = keyboardControl(key_input)


if __name__ == '__main__':
    main()