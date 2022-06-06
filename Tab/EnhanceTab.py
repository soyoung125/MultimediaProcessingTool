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

        plt.figure(figsize=(4, 5))
        plt.axis('off')
        plt.imshow(im_equalization)
        plt.savefig('./Images/Histogram_Equalization.png')

        img2 = imread('./Images/Histogram_Equalization.png')
        self.show_image(self.lblImage2_E, img2)

