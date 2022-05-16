from PyQt5.QtWidgets import QMainWindow
from ImprovementTap import ImprovementTap

class image_processing_class(QMainWindow):
    def __init__(self):
        from PyQt5.uic import loadUi
        super(image_processing_class, self).__init__()
        loadUi('image_processing_app.ui', self)
        self.image_source = None
        self.source_image = None

        # Tab improvement
        self.bntImpOpenImage_2.clicked.connect(lambda: self.open_image2())
        self.bntImpOpenImage.clicked.connect(lambda: self.open_image())
        self.bntShowRotate.clicked.connect(lambda: ImprovementTap.show_rotate(self))
        self.bntShowScaling.clicked.connect(lambda: ImprovementTap.show_scaling(self))
        self.bntshowFlip.clicked.connect(lambda: ImprovementTap.show_flip(self))
        self.bntShowWrap.clicked.connect(lambda: ImprovementTap.show_wrap(self))
        self.bntShowHistogram.clicked.connect(lambda: ImprovementTap.show_histogram(self))
        self.bntShowGrayscale.clicked.connect(lambda: ImprovementTap.show_grayscale(self))

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

    def show_image(self, label, image):
        import qimage2ndarray
        from PyQt5 import QtGui
        try:
            img = qimage2ndarray.array2qimage(image)
            qpixmap = QtGui.QPixmap.fromImage(img)
            label.setPixmap(qpixmap)
        except Exception as e:
            print('Error: {}'.format(e))


def image_processing_app():
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = image_processing_class()
    window.show()
    app.exec()


if __name__ == "__main__":
    image_processing_app()