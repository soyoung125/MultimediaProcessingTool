class TransformationTab():
    def __init__(self):
        pass

    def show_histogram(self):
        from matplotlib import pyplot as plt
        from skimage import io
        plt.figure(figsize=(5,4))
        plt.hist(self.source_image.ravel(), bins=256)
        plt.savefig('Hist.png')
        img2 =io.imread('Hist.png')
        self.show_image(self.lblImage2_2, img2)


    def show_grayscale(self):
        from skimage.color import rgb2gray
        from skimage.io import imread
        import matplotlib.pyplot as plt

        gray_image = rgb2gray(self.source_image)
        plt.figure(figsize=(5,4)), plt.axis('off')
        plt.imshow(gray_image, cmap='gray', vmin=0, vmax=1)
        plt.savefig('Invert.png')
        img2 = imread('Invert.png')
        self.show_image(self.lblImage2_2, img2)

    def save_JPEG(self):
        from PIL import Image
        import matplotlib.pyplot as plt
        from skimage.io import imread

        im = Image.open(self.image_source)
        plt.imshow(im)
        plt.savefig('saveJPEG.jpeg')
        img2 = imread('saveJPEG.jpeg')
        self.show_image(self.lblImage2_2, img2)

    def save_PNG(self):
        from PIL import Image
        import matplotlib.pyplot as plt
        from skimage.io import imread

        im = Image.open(self.image_source)
        plt.imshow(im)
        plt.savefig('savePNG.png')
        img2 = imread('savePNG.png')
        self.show_image(self.lblImage2_2, img2)

    def save_BMP(self):
        from PIL import Image
        import matplotlib.pyplot as plt
        from skimage.io import imread

        im = Image.open(self.image_source)
        plt.imshow(im)
        plt.savefig('saveBMP.bmp')
        img2 = imread('saveBMP.bmp')
        self.show_image(self.lblImage2_2, img2)