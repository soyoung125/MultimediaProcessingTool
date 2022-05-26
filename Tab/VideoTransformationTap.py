from numpy import random


class VideoTransformationTap:
    def __init__(self):
        pass

    def video_flip(self):
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
            resize_video = cv2.resize(video1, (320, 180), interpolation=cv2.INTER_CUBIC)
            cols, rows = resize_video.shape[:2]
            rot = cv2.getRotationMatrix2D((rows/2, cols/2), angle, 1)
            video_rotate = cv2.warpAffine(resize_video, rot, (0, 0))
            self.show_image(self.lblVideo2, video_rotate)

            cv2.waitKey(24)

        cap.release()
        cv2.destroyAllWindows()

    # Counting People
    def count_people(self):
        import cv2

        cap = cv2.VideoCapture(0)

        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        while True:
            ret, frame = cap.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            if not ret:
                break

            # 매 프레임마다 사람 검출
            detected, _ = hog.detectMultiScale(frame)  # 사각형 정보를 받아옴

            # 검출 결과 화면 표시
            person = 1
            for (x, y, w, h) in detected:
                c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                person += 1

            cv2.putText(frame, f'Total Persons : {person - 1}', (40, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
            self.show_image(self.lblVideo2, frame)

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



