class VideoTransformationTap:
    def __init__(self):
        pass

    def video_filp(self):
        import cv2

        video = cv2.VideoCapture(self.video_source)

        direction = self.cnndgrees.currentText()

        if direction == '90':
            angle = 90.0
        elif direction == '180':
            angle = 180.0
        elif direction == '270':
            angle = 270.0

        while True:
            ret, video1 = video.read()
            video1 = cv2.cvtColor(video1, cv2.COLOR_BGR2RGB)
            resize_video = cv2.resize(video1, (180, 320), interpolation=cv2.INTER_CUBIC)
            rows, cols = resize_video.shape[:2]
            rot = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
            video_rotate = cv2.warpAffine(resize_video, rot, (0, 0))
            # video_rotate = cv2.resize(video1, (320, 180), interpolation=cv2.INTER_CUBIC)
            self.show_image(self.lblVideo2, video_rotate)

            cv2.waitKey(24)

        cap.release()
        cv2.destroyAllWindows()

    def video_grayscale(self):
        import cv2

        video = cv2.VideoCapture(self.video_source)

        while True:
            ret, img = video.read()

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            self.show_image(self.lblVideo2, gray)
            cv2.waitKey(24)

        video.release()
        cv2.destroyAllWindows()