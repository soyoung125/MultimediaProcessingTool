from PyQt5.QtWidgets import QMainWindow
import os
import cv2
from PyQt5 import QtWidgets, QtCore
from skimage import io

from Tab.CountPersonTap import CountPersonTap
from Tab.EnhanceTap import EnhanceTap
from Tab.FilterTap import FilterTap
from Tab.ImprovementTap import ImprovementTap
from Tab.VideoTransformationTap import VideoTransformationTap
from Tab.TransformationTab import TransformationTab
from Tab.SaveTab import SaveTab

class image_processing_class(QMainWindow):
    def __init__(self):
        from PyQt5.uic import loadUi
        super(image_processing_class, self).__init__()
        loadUi('image_processing_app.ui', self)
        self.image_source = None
        self.source_image = None
        self.video_source = None

        # Tab improvement
        self.bntImpOpenImage.clicked.connect(lambda: self.open_image())
        self.bntShowRotate.clicked.connect(lambda: ImprovementTap.show_rotate(self))
        self.bntShowScaling.clicked.connect(lambda: ImprovementTap.show_scaling(self))
        self.bntshowFlip.clicked.connect(lambda: ImprovementTap.show_flip(self))
        self.bntShowWrap.clicked.connect(lambda: ImprovementTap.show_wrap(self))

        # Tab Transformation
        self.bntTransOpenImage.clicked.connect(lambda: self.open_image2())
        self.bntShowHistogram.clicked.connect(lambda: TransformationTab.show_histogram(self))
        self.bntShowGrayscale.clicked.connect(lambda: TransformationTab.show_grayscale(self))

        # Tab Save
        self.bntsavOpenImage.clicked.connect(lambda: self.open_image5())
        self.btnSaveJPEG.clicked.connect(lambda: SaveTab.save_JPEG(self))
        self.btnSavePNG.clicked.connect(lambda: SaveTab.save_PNG(self))
        self.btnSaveBMP.clicked.connect(lambda: SaveTab.save_BMP(self))

        # Tap Enhance
        self.btnehnopenimage.clicked.connect(lambda: self.open_image3())
        self.btnhisto_equal.clicked.connect(lambda: EnhanceTap.histogram_equalization(self))

        # Tap Filter
        self.btnFilterOpenImage.clicked.connect(lambda: self.open_image4())
        self.btnBlur.clicked.connect(lambda: FilterTap.show_blur(self))
        self.btnSmoothing.clicked.connect(lambda: FilterTap.show_smooth(self))
        self.btnSharpening.clicked.connect(lambda: FilterTap.show_sharp(self))

        # Tap VideoTransformation
        self.btnOpenVideo.clicked.connect(lambda: self.open_video())
        self.btnVideoFlip.clicked.connect(lambda: VideoTransformationTap.video_flip(self))
        self.btnGrayScale.clicked.connect(lambda: VideoTransformationTap.video_grayscale(self))
        self.btnConnectWebcam.clicked.connect(lambda: self.connect_webcam())
        self.btnStopWebcam.clicked.connect(lambda: self.stopwebcam())

        # Tap CountPerson
        self.btnCountPeople.clicked.connect(lambda: CountPersonTap.count_people(self))

    def open_image(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', QtCore.QDir.rootPath(),'*.*')
        try:
            self.image_source = fileName
            self.source_image = io.imread(fileName)
            self.show_image(self.lblImage1, self.source_image)
        except Exception as e:
            print('Error: {'.format(e))

    def open_image2(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', QtCore.QDir.rootPath(),'*.*')
        try:
            self.image_source = fileName
            self.source_image = io.imread(fileName)
            self.show_image(self.lblImage1_2, self.source_image)
        except Exception as e:
            print('Error: {'.format(e))

    def open_image3(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', QtCore.QDir.rootPath(),'*.*')
        try:
            self.image_source = fileName
            self.source_image = io.imread(fileName)
            self.show_image(self.lblImage1_E, self.source_image)
        except Exception as e:
            print('Error: {'.format(e))

    def open_image4(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', QtCore.QDir.rootPath(),'*.*')
        try:
            self.image_source = fileName
            self.source_image = io.imread(fileName)
            self.show_image(self.lblImage1_F, self.source_image)
        except Exception as e:
            print('Error: {'.format(e))

    def open_image5(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', QtCore.QDir.rootPath(), '*.*')
        try:
            self.image_source = fileName
            self.source_image = io.imread(fileName)
            self.show_image(self.lblImage1_Save, self.source_image)
        except Exception as e:
            print('Error: {'.format(e))

    def show_image(self, label, image):
        import qimage2ndarray
        from PyQt5 import QtGui
        try:
            img = qimage2ndarray.array2qimage(image)
            qpixmap = QtGui.QPixmap.fromImage(img)
            label.setPixmap(qpixmap)
        except Exception as e:
            print('Error: {}'.format(e))

    def open_video(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', QtCore.QDir.rootPath(), '*.*')
        cap = cv2.VideoCapture(fileName)
        self.video_source = fileName

        while True:
            ret, self.image_source = cap.read()
            self.image_source = cv2.cvtColor(self.image_source, cv2.COLOR_BGR2RGB)
            resize_video = cv2.resize(self.image_source, (320, 180), interpolation=cv2.INTER_CUBIC)
            self.show_image(self.lblVideo1, resize_video)

            cv2.waitKey(24)

        cap.release()
        cv2.destroyAllWindows()

    def connect_webcam(self):
        self.stop_webcam = False
        # self.blur_flag = False
        cap = cv2.VideoCapture(0)
        while True:
            ret, self.source_image = cap.read()
            self.source_image = cv2.cvtColor(self.source_image, cv2.COLOR_BGR2RGB)
            self.show_image(self.lblVideo1, self.source_image)
            # if self.blur_flag:
            #     blur_image = cv2.blur(self.source_image, (9,9))
            #     self.show_image(self.lblVideo1, blur_image)
            cv2.waitKey(24)
            if self.stop_webcam:
                break
        cap.release()
        cv2.destroyAllWindows()

    def stopwebcam(self):
        self.stop_webcam =True

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

def image_processing_app():
    import sys
    from PyQt5.QtWidgets import QApplication

    createFolder('./Images')

    app = QApplication(sys.argv)
    window = image_processing_class()
    window.show()
    app.exec()


if __name__ == "__main__":
    image_processing_app()