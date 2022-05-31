import cv2
import numpy as np

# opencv가 감지할 수 있는 mouse event 확인하기
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

click = False  # Mouse 클릭된 상태 (false = 클릭 x / true = 클릭 o) : 마우스 눌렀을때 true로, 뗏을때 false로
x1, y1 = -1, -1
x2, y2 = -1, -1

class OpenNewScreen:
    def __init__(self):
        pass

    def open_screen(self, image_source):
        open_img(image_source)
        cv2.destroyAllWindows()
        return (x1, y1, x2, y2)


def open_img(img_sc):
    global img, img1
    global im_source
    im_source = img_sc
    img = cv2.imread(im_source)
    img1 = cv2.imread(im_source)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_rectangle)
    # main문 : 키보드로 esc를 받을때까지 화면을 계속 보여준다.
    while True:
        cv2.putText(img, "After setting the crop range,", (5,20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.putText(img, "press the esc key.", (5, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (0, 0, 255), 1, cv2.LINE_AA)
        cv2.imshow('image', img)  # 화면을 보여준다.

        k = cv2.waitKey(1) & 0xFF  # 키보드 입력값을 받고

        if k == 27:  # esc를 누르면 종료
            break

# Mouse Callback함수 : 파라미터는 고정됨.
def draw_rectangle(event, x, y, flags, param):
    global x1, y1, click, x2, y2  # 전역변수 사용
    global img, img1, im_source

    if event == cv2.EVENT_LBUTTONDOWN:  # 마우스를 누른 상태
        click = True
        x1, y1 = x, y
        img = cv2.imread(im_source)
        img1 = cv2.imread(im_source)
        cv2.rectangle(img, (x1, y1), (x, y), (255, 0, 0), 10)
        print("사각형의 왼쪽위 설정 : (" + str(x1) + ", " + str(y1) + ")")

    elif event == cv2.EVENT_MOUSEMOVE:  # 마우스 이동
        if click == True:  # 마우스를 누른 상태 일경우
            img = cv2.imread(im_source)
            cv2.rectangle(img, (x1, y1), (x, y), (255, 0, 0), 6)
            print("(" + str(x1) + ", " + str(y1) + "), (" + str(x) + ", " + str(y) + ")")

    elif event == cv2.EVENT_LBUTTONUP:
        click = False;  # 마우스를 때면 상태 변경
        img = img1
        x2, y2 = x,y
        cv2.rectangle(img, (x1, y1), (x, y), (255, 0, 0), 6)
