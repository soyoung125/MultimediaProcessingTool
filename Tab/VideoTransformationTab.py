from numpy import random


class VideoTransformationTab:
    def __init__(self):
        pass

    def video_flip(self):
        import cv2
        self.grayscale_flag = False
        self.flip_flag = True

        video = cv2.VideoCapture(self.video_source)

        direction = self.cnndgrees.currentText()

        if direction == '90':
            angle = 90.0
        elif direction == '180':
            angle = 180.0
        elif direction == '270':
            angle = 270.0

        while True:
            if self.flip_flag == False:
                break
            ret, video1 = video.read()
            video1 = cv2.cvtColor(video1, cv2.COLOR_BGR2RGB)
            resize_video = cv2.resize(video1, (540, 560), interpolation=cv2.INTER_CUBIC)
            cols, rows = resize_video.shape[:2]
            rot = cv2.getRotationMatrix2D((rows/2, cols/2), angle, 1)
            video_rotate = cv2.warpAffine(resize_video, rot, (0, 0))
            self.show_image(self.lblVideo2, video_rotate)

            cv2.waitKey(24)

        video.release()
        cv2.destroyAllWindows()

    def webcam_flip(self):
        self.grayscale_flag = False
        self.flip_flag = True
        direction = self.cnndgrees.currentText()

        if direction == '90':
            self.angle = 90.0
        elif direction == '180':
            self.angle = 180.0
        elif direction == '270':
            self.angle = 270.0

    def grayscale(self):
        self.flip_flag = False
        self.grayscale_flag = True
