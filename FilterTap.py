class FilterTap():
    def __init__(self):
        pass

    def show_blur(self):
        from PIL import Image
        import matplotlib.pyplot as plt
        from skimage import filters, io
        from skimage.io import imread

        im = io.imread(self.image_source)
        sigma = int(self.txtSigma.toPlainText())
        im_blur = filters.gaussian(im, sigma=sigma, channel_axis=-1)
        plt.figure(figsize=(4, 5))
        plt.axis('off')
        plt.imshow(im_blur)
        plt.savefig('BlurImage.png')

        img2 = imread('BlurImage.png')
        self.show_image(self.lblImage2_F, img2)

    #def show_smooth(self):


    #def show_sharp(self):

