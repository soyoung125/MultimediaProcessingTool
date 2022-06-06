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
        self.grayscale_flag = False
        self.stop_video = True

        # Tab improvement
        self.bntImpOpenImage.clicked.connect(lambda: self.open_image())
        self.bntShowRotate.clicked.connect(lambda: ImprovementTap.show_rotate(self))
        self.bntShowScaling.clicked.connect(lambda: ImprovementTap.show_scaling(self))
        self.bntshowFlip.clicked.connect(lambda: ImprovementTap.show_flip(self))
        self.bntShowWrap.clicked.connect(lambda: ImprovementTap.show_warp(self))
        self.btnShowCrop.clicked.connect(lambda: ImprovementTap.click_crop(self))

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
        self.btnConnectWebcam.clicked.connect(lambda: self.connectwebcam())
        self.btnStopWebcam.clicked.connect(lambda: self.stopwebcam())
        self.btnVideoFlip.clicked.connect(lambda: VideoTransformationTap.video_flip(self))
        self.btnWebcamFlip.clicked.connect(lambda: VideoTransformationTap.webcam_flip(self))
        self.btnGrayScale.clicked.connect(lambda: VideoTransformationTap.grayscale(self))


        # Tap CountPerson
        self.btnCountPeople.clicked.connect(lambda: CountPersonTap.count_people(self))

    def open_image(self):
        from PyQt5 import QtWidgets, QtCore
        from skimage import io
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', QtCore.QDir.rootPath(),'*.*')
        try:
            self.image_source = fileName
            self.source_image = io.imread(fileName)
            self.show_image(self.lblImage1, self.source_image)
        except Exception as e:
            print('Error: {'.format(e))

    def open_image2(self):
        from PyQt5 import QtWidgets, QtCore
        from skimage import io
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', QtCore.QDir.rootPath(),'*.*')
        try:
            self.image_source = fileName
            self.source_image = io.imread(fileName)
            self.show_image(self.lblImage1_2, self.source_image)
        except Exception as e:
            print('Error: {'.format(e))

    def open_image3(self):
        from PyQt5 import QtWidgets, QtCore
        from skimage import io
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', QtCore.QDir.rootPath(),'*.*')
        try:
            self.image_source = fileName
            self.source_image = io.imread(fileName)
            self.show_image(self.lblImage1_E, self.source_image)
        except Exception as e:
            print('Error: {'.format(e))

    def open_image4(self):
        from PyQt5 import QtWidgets, QtCore
        from skimage import io
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', QtCore.QDir.rootPath(),'*.*')
        try:
            self.image_source = fileName
            self.source_image = io.imread(fileName)
            self.show_image(self.lblImage1_F, self.source_image)
        except Exception as e:
            print('Error: {'.format(e))

    def open_image5(self):
        from PyQt5 import QtWidgets, QtCore
        from skimage import io
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
        import cv2
        from PyQt5 import QtWidgets, QtCore

        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', QtCore.QDir.rootPath(), '*.*')
        cap = cv2.VideoCapture(fileName)
        self.video_source = fileName
        self.stop_webcam = True
        self.stop_video = False

        while True:
            ret, self.source_image = cap.read()
            self.source_image = cv2.cvtColor(self.source_image, cv2.COLOR_BGR2RGB)
            resize_video = cv2.resize(self.source_image, (320, 180), interpolation=cv2.INTER_CUBIC)
            self.show_image(self.lblVideo1, resize_video)

            if self.grayscale_flag:
                print(1)
                gray = cv2.cvtColor(self.source_image, cv2.COLOR_BGR2GRAY)
                resize_gray_video = cv2.resize(gray, (320, 180), interpolation=cv2.INTER_CUBIC)
                self.show_image(self.lblVideo2, resize_gray_video)

            cv2.waitKey(24)
            if self.stop_video:
                break

        cap.release()
        cv2.destroyAllWindows()

    def connectwebcam(self):
        self.stop_video = True
        self.stop_webcam = False
        self.grayscale_flag = False
        self.flip_flag = False
        self.angle = 0
        cap = cv2.VideoCapture(0)
        while True:
            ret, self.source_image = cap.read()
            self.source_image = cv2.cvtColor(self.source_image, cv2.COLOR_BGR2RGB)
            self.show_image(self.lblVideo1, self.source_image)

            if self.flip_flag:
                cols, rows = self.source_image.shape[:2]
                rot = cv2.getRotationMatrix2D((rows / 2, cols / 2), self.angle, 1)
                webcam_rotate = cv2.warpAffine(self.source_image, rot, (0, 0))
                self.show_image(self.lblVideo2, webcam_rotate)

            cv2.waitKey(24)

            if self.grayscale_flag:
                gray = cv2.cvtColor(self.source_image, cv2.COLOR_BGR2GRAY)
                self.show_image(self.lblVideo2, gray)
            cv2.waitKey(24)
            if self.stop_webcam:
                break


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