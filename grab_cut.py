import numpy as np
import cv2


class Grab_cut(object):
    suffix = '.jpg'

    def __init__(self, filename=None):
        self.filename = filename
        self.height = None
        self.width = None

    def image_matting(self, image_file, shape, iteration=10):
        points = shape['points']
        xmin, ymin, xmax, ymax = Grab_cut.convertPoints2BndBox(points)
        self.width = xmax - xmin
        self.height = ymax - ymin

        src_img = cv2.imread(image_file)

        mask = np.zeros(src_img.shape[:2], np.uint8)
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)
        rect = (xmin, ymin, self.width, self.height)

        # Grabcut
        cv2.grabCut(src_img, mask, rect, bgdModel, fgdModel,
                    iteration, cv2.GC_INIT_WITH_RECT)

        r_channel, g_channel, b_channel = cv2.split(src_img)
        a_channel = np.where((mask == 2) | (mask == 0), 0, 255).astype('uint8')

        # crop image space
        for row in range(ymin, ymax):
            if sum(r_channel[row, xmin:xmax + 1]) > 0:
                out_ymin = row
                break
        for row in range(ymin, ymax)[::-1]:
            if sum(r_channel[row, xmin:xmax + 1]) > 0:
                out_ymax = row + 1
                break
        for col in range(xmin, xmax):
            if sum(a_channel[ymin:ymax + 1, col]) > 0:
                out_xmin = col
                break
        for col in range(xmin, xmax)[::-1]:
            if sum(a_channel[ymin:ymax + 1, col]) > 0:
                out_xmax = col + 1
                break

        # output image
        img_RGBA = cv2.merge((r_channel[out_ymin:out_ymax, out_xmin:out_xmax],
                              g_channel[out_ymin:out_ymax, out_xmin:out_xmax],
                              b_channel[out_ymin:out_ymax, out_xmin:out_xmax],
                              a_channel[out_ymin:out_ymax, out_xmin:out_xmax]))

        return img_RGBA

    @staticmethod
    def convertPoints2BndBox(points):
        xmin = float('inf')
        ymin = float('inf')
        xmax = float('-inf')
        ymax = float('-inf')
        for p in points:
            x = p[0]
            y = p[1]
            xmin = min(x, xmin)
            ymin = min(y, ymin)
            xmax = max(x, xmax)
            ymax = max(y, ymax)

        # Martin Kersner, 2015/11/12
        # 0-valued coordinates of BB caused an error while
        # training faster-rcnn object detector.
        if xmin < 1:
            xmin = 1

        if ymin < 1:
            ymin = 1

        return (int(xmin), int(ymin), int(xmax), int(ymax))

    @staticmethod
    def resultSave(save_path, image_np):
        cv2.imwrite(save_path, image_np)
