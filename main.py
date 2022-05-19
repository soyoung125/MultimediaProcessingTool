from PyQt5.QtWidgets import QMainWindow

from EnhanceTap import EnhanceTap
from FilterTap import FilterTap
from ImprovementTap import ImprovementTap

class image_processing_class(QMainWindow):
    def __init__(self):
        from PyQt5.uic import loadUi
        super(image_processing_class, self).__init__()
        loadUi('image_processing_app.ui', self)
        self.image_source = None
        self.source_image = None
        self.source_video = None

        # Tab improvement
        self.bntImpOpenImage_2.clicked.connect(lambda: self.open_image2())
        self.bntImpOpenImage.clicked.connect(lambda: self.open_image())
        self.bntShowRotate.clicked.connect(lambda: ImprovementTap.show_rotate(self))
        self.bntShowScaling.clicked.connect(lambda: ImprovementTap.show_scaling(self))
        self.bntshowFlip.clicked.connect(lambda: ImprovementTap.show_flip(self))
        self.bntShowWrap.clicked.connect(lambda: ImprovementTap.show_wrap(self))
        self.bntShowHistogram.clicked.connect(lambda: ImprovementTap.show_histogram(self))
        self.bntShowGrayscale.clicked.connect(lambda: ImprovementTap.show_grayscale(self))
        self.btnSaveJPEG.clicked.connect(lambda: ImprovementTap.save_JPEG(self))
        self.btnSavePNG.clicked.connect(lambda: ImprovementTap.save_PNG(self))
        self.btnSaveBMP.clicked.connect(lambda: ImprovementTap.save_BMP(self))

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
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', QtCore.QDir.rootPath(),'*.*')
        try:
            self.image_source = fileName
            self.source_image = io.imread(fileName)
            self.show_image(self.lblVideo1, self.source_image)
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
        from skimage import io

        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', QtCore.QDir.rootPath(), '*.*')
        cap = cv2.VideoCapture(fileName)

        while True:
            ret, self.image_source = cap.read()
            self.image_source = cv2.cvtColor(self.image_source, cv2.COLOR_BGR2RGB)
            self.show_image(self.lblVideo1, self.image_source)
            # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
            # w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            # h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            # print("변환된 동영상 너비(가로) : {}, 높이(세로) : {}".format(w, h))
            cv2.waitKey(24)
        cap.release()
        cv2.destroyAllWindows()

    # def show_video(self):

def image_processing_app():
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = image_processing_class()
    window.show()
    app.exec()


if __name__ == "__main__":
    image_processing_app()