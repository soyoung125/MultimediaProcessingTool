class ImprovementTap():
    def __init__(self):
        pass

    def show_rotate(self):
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

    def show_scaling(self):
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

    def show_flip(self):
        from PIL import Image
        import matplotlib.pyplot as plt
        from skimage.io import imread

        im = Image.open(self.image_source)

        direction = self.cbbImpFlip.currentText()

        if direction == 'Top-Bottom':
            im_Flip = im.transpose(Image.FLIP_TOP_BOTTOM)
        elif direction == 'Left-Right':
            im_Flip = im.transpose(Image.FLIP_LEFT_RIGHT)

        plt.figure(figsize=(5, 4)), plt.axis('off')
        plt.imshow(im_Flip)
        plt.savefig('Flip.png')

        img2 = imread('Flip.png')
        self.show_image(self.lblImage2, img2)

    def show_wrap(self):
        import numpy as np
        from PIL import Image
        import math
        import matplotlib.pyplot as plt
        from skimage.io import imread

        img = Image.open(self.image_source).convert("L")
        img = np.array(img)
        rows, cols = img.shape[0], img.shape[1]
        img_output = np.zeros((rows, cols))

        print(self.rbImpHorizontal.isChecked())

        if self.rbImpHorizontal.isChecked():
            for i in range(rows):
                for j in range(cols):
                    offset_x = int(40.0 * math.sin(2 * 3.14 * i / 180))
                    if j + offset_x < rows:
                        img_output[i, j] = img[i, (j + offset_x) % cols]
                    else:
                        img_output[i, j] = 0
        elif self.rvImpVertical.isChecked():
            for i in range(rows):
                for j in range(cols):
                    offset_y = int(40.0 * math.sin(2 * 3.14 * j / 180))
                    if i + offset_y < rows:
                        img_output[i, j] = img[(i + offset_y) % rows, j]
                    else:
                        img_output[i, j] = 0

        plt.figure(figsize=(5, 4)), plt.axis('off')
        plt.imshow(img_output, cmap='gray')
        plt.savefig('Wrap.png')

        img2 = imread('Wrap.png')
        self.show_image(self.lblImage2, img2)

    def show_histogram(self):
        from matplotlib import pyplot as plt
        from skimage import io
        plt.figure(figsize=(5,4))
        plt.hist(self.source_image.ravel(), bins=256)
        plt.savefig('hist.png')
        hist_img =io.imread('hist.png')
        self.show_image(self.lblImage2_2, hist_img)