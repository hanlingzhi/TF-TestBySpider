import imutils, skimage
import cv2


class OpenCVSSIM(object):

    i_a, i_b, i_diff = None, None, None

    c_diff = None

    def __init__(self, image_a, image_b, image_diff):
        self.i_a = cv2.imread(image_a)
        self.i_b = cv2.imread(image_b)
        self.i_diff = image_diff

    def compare_images(self):
        i_a_gray = cv2.cvtColor(self.i_a, cv2.COLOR_BGR2GRAY)
        i_b_gray = cv2.cvtColor(self.i_b, cv2.COLOR_BGR2GRAY)
        (c_score, c_diff) = skimage.metrics.structural_similarity(i_a_gray, i_b_gray, full=True)
        self.c_diff = (c_diff * 255).astype("uint8")
        return c_score

    def output_diff(self):
        thresh = cv2.threshold(self.c_diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnt_s = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnt_s = cnt_s[1] if imutils.is_cv3() else cnt_s[0]
        # 划差异区域
        for c in cnt_s:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(self.i_a, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(self.i_b, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imwrite(self.i_diff, self.i_b)
        cv2.waitKey(0)
