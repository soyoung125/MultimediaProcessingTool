class FilterTap():
    def __init__(self):
        pass

    def show_blur(self):
        from PIL import Image
        import matplotlib.pyplot as plt
        from skimage import filters, io
        from skimage.io import imread

        img = io.imread(self.image_source)
        sigma = int(self.txtSigma.toPlainText())
        im_blur = filters.gaussian(img, sigma=sigma, channel_axis=-1)
        plt.figure(figsize=(4, 5))
        plt.axis('off')
        plt.imshow(im_blur)
        plt.savefig('BlurImage.png')

        img2 = imread('BlurImage.png')
        self.show_image(self.lblImage2_F, img2)

    def show_smooth(self):
        import cv2
        import numpy as np
        import matplotlib.pyplot as plt
        from skimage import filters, io
        from skimage.io import imread

        img = io.imread(self.image_source)

        smoothing_mask = np.array([[1 / 16, 1 / 8, 1 / 16], [1 / 8, 1 / 4, 1 / 8], [1 / 16, 1 / 8, 1 / 16]])
        im_smooth = cv2.filter2D(img, -1, smoothing_mask)

        plt.figure(figsize=(4, 5))
        plt.axis('off')
        plt.imshow(im_smooth)
        plt.savefig('SmoothImage.png')

        img2 = imread('SmoothImage.png')

        self.show_image(self.lblImage2_F, img2)

        # pip uninstall opencv-contrib-python
        # pip install opencv-contrib-python    cv2 오류 발생시 설치 필요

    # def show_sharp(self):
