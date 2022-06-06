import os


class CountPersonTab:
    def __init__(self):
        pass

    def count_people(self):
        # !python yolov5/detect.py --weights best.pt --img 416 --conf 0.1 --source 0
        os.system("python yolov5/detect.py --weights best.pt --img 416 --conf 0.1 --source 0")
