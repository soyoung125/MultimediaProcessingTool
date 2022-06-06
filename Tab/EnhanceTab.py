class EnhanceTab():
    def __init__(self):
        pass

    def histogram_equalization(self):
        from PIL import Image
        from skimage import io, exposure
        from matplotlib import pyplot as plt
        from skimage.io import imread

        im = io.imread(self.image_source)

        im_equalization = exposure.equalize_hist(im)

        plt.figure(figsize=(6, 6))
        plt.axis('off')
        plt.imshow(im_equalization)
        plt.savefig('./Images/Histogram_Equalization.png')

        img2 = imread('./Images/Histogram_Equalization.png')
        self.show_image(self.lblImage2_E, img2)

    def gamma_correction(self):
        import cv2
        import numpy as np
        from matplotlib import pyplot as plt
        from skimage.io import imread

        gamma = self.dsGamma.value()
        img = cv2.imread(self.image_source)
        out = img.astype(np.float)
        out = ((out / 255) ** (1 / gamma)) * 255
        out = out.astype(np.uint8)

        plt.figure(figsize=(6, 6))
        plt.axis('off')
        plt.imshow(out)
        plt.savefig('./Images/GammaCorrection.png')

        img2 = imread('./Images/GammaCorrection.png')
        self.show_image(self.lblImage2_E, img2)