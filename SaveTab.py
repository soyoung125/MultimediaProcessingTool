class SaveTab():
    def __init__(self):
        pass


    def save_JPEG(self):
        from PIL import Image
        import matplotlib.pyplot as plt
        from skimage.io import imread

        im = Image.open(self.image_source)
        plt.imshow(im)
        plt.savefig('saveJPEG.jpeg')
        img2 = imread('saveJPEG.jpeg')
        self.show_image(self.lblImage2_Save, img2)


    def save_PNG(self):
        from PIL import Image
        import matplotlib.pyplot as plt
        from skimage.io import imread

        im = Image.open(self.image_source)
        plt.imshow(im)
        plt.savefig('savePNG.png')
        img2 = imread('savePNG.png')
        self.show_image(self.lblImage2_Save, img2)


    def save_BMP(self):
        from PIL import Image
        import matplotlib.pyplot as plt
        from skimage.io import imread

        im = Image.open(self.image_source)
        plt.imshow(im)
        plt.savefig('saveBMP.bmp')
        img2 = imread('saveBMP.bmp')
        self.show_image(self.lblImage2_Save, img2)