import cv2
from canva import Canva

WINDOWS_NAME : str = 'K-mean'
WIDTH: int = 1000
HEIGHT: int = 600

c = Canva(WIDTH, HEIGHT)

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


def nothing(args):
    pass

class Param:
    def __init__(self):
        self.color=0


def main():
    p = Param()
    cv2.namedWindow(WINDOWS_NAME)
    cv2.createTrackbar('color', WINDOWS_NAME, 0, 2, nothing)
    cv2.setMouseCallback(WINDOWS_NAME, mouseControl, p)

    main_loop = True
    while main_loop:
        p.color = cv2.getTrackbarPos('color', WINDOWS_NAME)
        cv2.imshow(WINDOWS_NAME, c.frame)
        key_input = cv2.waitKey(1) & 0xFF
        main_loop = keyboardControl(key_input)


if __name__ == '__main__':
    main()