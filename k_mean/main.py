import cv2
from canva import Canva

WINDOWS_NAME : str = 'K-mean'
WIDTH: int = 1000
HEIGHT: int = 600


def mouseControl(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pass
    else:
        pass


def keyboardControl(key):
    if key == ord('q'):
        cv2.destroyAllWindows()
        return False
    return True


def nothing(args):
    pass


def main():
    c = Canva(WIDTH,HEIGHT)
    cv2.namedWindow(WINDOWS_NAME)
    cv2.setMouseCallback(WINDOWS_NAME, mouseControl)
    cv2.createTrackbar('color', WINDOWS_NAME, 0, 2, nothing)

    main_loop = True
    while main_loop:
        color = cv2.getTrackbarPos('color', WINDOWS_NAME)
        cv2.imshow(WINDOWS_NAME, c.canvas)
        key_input = cv2.waitKey(1) & 0xFF
        main_loop = keyboardControl(key_input)


if __name__ == '__main__':
    main()