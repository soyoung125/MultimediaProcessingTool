class SaveTab():
    def __init__(self):
        pass


    def save_JPEG(self):
        from PIL import Image
        import matplotlib.pyplot as plt
        from skimage.io import imread

        im = Image.open(self.image_source)
        plt.imshow(im)
        im.save('saveJPEG.jpeg', "JPEG")
        img2 = imread('saveJPEG.jpeg')
        self.show_image(self.lblImage2_Save, img2)


    def save_PNG(self):
        from PIL import Image
        import matplotlib.pyplot as plt
        from skimage.io import imread

        im = Image.open(self.image_source)
        plt.imshow(im)
        im.save('savePNG.png', "PNG")
        img2 = imread('savePNG.png')
        self.show_image(self.lblImage2_Save, img2)


    def save_BMP(self):
        from PIL import Image
        import matplotlib.pyplot as plt
        from skimage.io import imread

        im = Image.open(self.image_source)
        plt.imshow(im)
        im.save('saveBMP.bmp', "BMP")
        img2 = imread('saveBMP.bmp')
        self.show_image(self.lblImage2_Save, img2)