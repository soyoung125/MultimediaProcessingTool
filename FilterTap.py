class FilterTap():
    def __init__(self):
        pass

    def show_blur(self):
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

    def show_sharp(self):
        import cv2
        import numpy as np
        import matplotlib.pyplot as plt
        from skimage import io
        from skimage.io import imread
        from PIL import Image

        img = io.imread(self.image_source)

        direction = self.cbbSharp.currentText()

        if direction == '1':
            sharpening_mask = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
        elif direction == '3':
            sharpening_mask = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        elif direction == '5':
            sharpening_mask = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        elif direction == '7':
            sharpening_mask = np.array([[-1, -1, 0], [-1, 7, -1], [0, -1, -1]])
        elif direction == '9':
            sharpening_mask = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

        # sharpening_mask = np.array([[0 for j in range(3)] for i in range(3)])
        # nsum = 0
        # sigma_sharp = int(self.txtSharp.toPlainText())
        # sharpening_mask[1][1] = sigma_sharp
        #
        # for i in range(0, 2):
        #     for j in range(0, 2):
        #         nsum = nsum + sharpening_mask[i][j]
        #
        # while nsum != 1:
        #     sharpening_mask[1][0] = sharpening_mask[1][0] - 1
        #     sharpening_mask[1][2] = sharpening_mask[1][2] - 1
        #     sharpening_mask[0][1] = sharpening_mask[0][1] - 1
        #     sharpening_mask[2][1] = sharpening_mask[2][1] - 1
        #     sharpening_mask[0][0] = sharpening_mask[0][0] - 1
        #     sharpening_mask[0][2] = sharpening_mask[0][2] - 1
        #     sharpening_mask[2][0] = sharpening_mask[2][0] - 1
        #     sharpening_mask[2][2] = sharpening_mask[2][2] - 1

        im_sharp = cv2.filter2D(img, -1, sharpening_mask)

        plt.figure(figsize=(4, 5))
        plt.axis('off')
        plt.imshow(im_sharp)
        plt.savefig('SharpImage.png')

        img2 = imread('SharpImage.png')

        self.show_image(self.lblImage2_F, img2)
