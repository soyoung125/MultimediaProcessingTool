class TransformationTab():
    def __init__(self):
        pass

    def show_histogram(self):
        from matplotlib import pyplot as plt
        from skimage import io
        plt.figure(figsize=(5,4))
        plt.hist(self.source_image.ravel(), bins=256)
        plt.savefig('./Images/Hist.png')
        img2 =io.imread('./Images/Hist.png')
        self.show_image(self.lblImage2_2, img2)


    def show_grayscale(self):
        from skimage.color import rgb2gray
        from skimage.io import imread
        import matplotlib.pyplot as plt

        gray_image = rgb2gray(self.source_image)
        plt.figure(figsize=(5,4)), plt.axis('off')
        plt.imshow(gray_image, cmap='gray', vmin=0, vmax=1)
        plt.savefig('./Images/Invert.png')
        img2 = imread('./Images/Invert.png')
        self.show_image(self.lblImage2_2, img2)

