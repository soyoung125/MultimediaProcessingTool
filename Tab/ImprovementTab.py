# import OpenNewScreen
from cv2 import imread
from matplotlib import pyplot as plt

from Tab.OpenNewScreen import OpenNewScreen


class ImprovementTab():
    def __init__(self):
        pass

    def show_rotate(self):
        from PIL import Image
        import matplotlib.pyplot as plt
        from skimage.io import imread

        im = Image.open(self.image_source)

        alpha = self.spImpAlpha.value()

        im_rotate = im.rotate(alpha)
        plt.figure(figsize=(6, 6)), plt.axis('off')
        plt.imshow(im_rotate, cmap='gray', vmin=0, vmax=1)
        plt.savefig('./Images/Rotate.png')

        img2 = imread('./Images/Rotate.png')
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

        plt.figure(figsize=(6, 6)), plt.axis('off')
        plt.imshow(im_size, cmap='gray', vmin=0, vmax=1)
        plt.savefig('./Images/Scaling.png')

        img2 = imread('./Images/Scaling.png')
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

        plt.figure(figsize=(6, 6)), plt.axis('off')
        plt.imshow(im_Flip)
        plt.savefig('./Images/Flip.png')

        img2 = imread('./Images/Flip.png')
        self.show_image(self.lblImage2, img2)

    def show_warp(self):
        import numpy as np
        from PIL import Image
        import math
        import matplotlib.pyplot as plt
        from skimage.io import imread

        img = Image.open(self.image_source).convert("L")
        img = np.array(img)
        rows, cols = img.shape[0], img.shape[1]
        img_output = np.zeros((rows, cols))

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

        plt.figure(figsize=(6, 6)), plt.axis('off')
        plt.imshow(img_output, cmap='gray')
        plt.savefig('./Images/Wrap.png')

        img2 = imread('./Images/Wrap.png')
        self.show_image(self.lblImage2, img2)

    def click_crop(self):
        img = imread(self.image_source)

        instance = OpenNewScreen()

        x1, y1, x2, y2 = instance.open_screen(self.image_source)

        croped_img = img[y1:y2, x1:x2]
        self.show_image(self.lblImage2, croped_img)
