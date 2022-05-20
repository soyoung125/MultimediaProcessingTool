class SaveTab():
    def __init__(self):
        pass


    def save_JPEG(self):
        from PIL import Image
        import matplotlib.pyplot as plt
        from skimage.io import imread

        im = Image.open(self.image_source)
        plt.imshow(im)
        im.save('./Images/saveJPEG.jpeg', "JPEG")
        img2 = imread('./Images/saveJPEG.jpeg')
        self.show_image(self.lblImage2_Save, img2)


    def save_PNG(self):
        from PIL import Image
        import matplotlib.pyplot as plt
        from skimage.io import imread

        im = Image.open(self.image_source)
        plt.imshow(im)
        im.save('./Images/savePNG.png', "PNG")
        img2 = imread('./Images/savePNG.png')
        self.show_image(self.lblImage2_Save, img2)


    def save_BMP(self):
        from PIL import Image
        import matplotlib.pyplot as plt
        from skimage.io import imread

        im = Image.open(self.image_source)
        plt.imshow(im)
        im.save('./Images/saveBMP.bmp', "BMP")
        img2 = imread('./Images/saveBMP.bmp')
        self.show_image(self.lblImage2_Save, img2)