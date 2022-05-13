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
        plt.savefig('Rotate.png')

        img2 = imread('Rotate.png')
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
        plt.savefig('Scaling.png')

        img2 = imread('Scaling.png')
        self.show_image(self.lblImage2, img2)

    def show_Flip(self):
        from PIL import Image
        import matplotlib.pyplot as plt
        from skimage.io import imread

        im = Image.open(self.image_source)

        direction = self.cbbImpFlip.currentText()

        if direction == 'Top':
            im_Flip = im.transpose(Image.FLIP_TOP_BOTTOM)
        elif direction == 'Bottom':
            im_Flip = im.transpose(Image.FLIP_TOP_BOTTOM)
        elif direction == 'Left':
            im_Flip = im.transpose(Image.FLIP_LEFT_RIGHT)
        elif direction == 'Right':
            im_Flip = im.transpose(Image.FLIP_LEFT_RIGHT)

        plt.figure(figsize=(5, 4)), plt.axis('off')
        plt.imshow(im_Flip)
        plt.savefig('Flip.png')

        img2 = imread('Flip.png')
        self.show_image(self.lblImage2, img2)