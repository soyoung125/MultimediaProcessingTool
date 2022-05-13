class ImprovementTap():
    def __init__(self):
        pass

    def show_Rotate(self):
        from PIL import Image
        import matplotlib.pyplot as plt
        from skimage.io import imread

        print(123)
        im = Image.open(self.image_source)

        alpha = self.spAlpha.value()
        print(alpha)

        im_rotate = im.rotate(alpha)
        plt.figure(figsize=(5, 4)), plt.axis('off')
        plt.imshow(im_rotate, cmap='gray', vmin=0, vmax=1)
        plt.savefig('invert.png')

        img2 = imread('invert.png')
        self.show_image(self.lblImage2, img2)