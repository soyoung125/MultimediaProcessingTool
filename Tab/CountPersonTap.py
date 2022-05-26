class CountPersonTap:
    def __init__(self):
        pass

    # Counting People
    def count_people(self):
        import numpy as np
        import cv2
        from matplotlib import pyplot as plt

        cap = cv2.VideoCapture(0)

        # hog = cv2.HOGDescriptor()
        # hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        while True:
            ret, frame = cap.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            if not ret:
                break

            faces = face_cascade.detectMultiScale(frame, 1.3, 5)

            # 검출 결과 화면 표시
            person = 1

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                person += 1

            cv2.putText(frame, f'Total Persons : {person - 1}', (40, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0),
                        2)
            self.show_image(self.lblcount, frame)

            cv2.waitKey(24)

        cap.release()
        cv2.destroyAllWindows()
