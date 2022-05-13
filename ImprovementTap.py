class ImprovementTap():
    def __init__(self):
        pass

    def show_Rotate(self):
        from PIL import Image
        import matplotlib.pyplot as plt
        from skimage.io import imread

        im = Image.open(self.image_source)

        alpha = self.spImpAlpha.value()
        print(alpha)

        im_rotate = im.rotate(alpha)
        plt.figure(figsize=(5, 4)), plt.axis('off')
        plt.imshow(im_rotate, cmap='gray', vmin=0, vmax=1)
        plt.savefig('invert.png')

        img2 = imread('invert.png')
        self.show_image(self.lblImage2, img2)

    def show_Scaling(self):
        from PIL import Image
        import matplotlib.pyplot as plt
        from skimage.io import imread

        im = Image.open(self.image_source)

        size0 = im.size[0], im.size[1]
        x = self.dsbImpX.value()
        y = self.dsbImpY.value()
        size1 = (x, y)
        im_size = im.resize((round(size0[0] * size1[0]), round(size0[1] * size1[1])))

        plt.figure(figsize=(5, 4)), plt.axis('off')
        plt.imshow(im_size, cmap='gray', vmin=0, vmax=1)
        plt.savefig('invert.png')

        img2 = imread('invert.png')
        self.show_image(self.lblImage2, img2)