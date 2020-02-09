
from PIL import Image
from PIL import ImageChops
from test_spider.util.print_format_util import PrintFormatUtil

class ImageSSIM(object):

    i_a, i_b, i_diff = None, None, None

    def __init__(self, image_a, image_b, image_diff):
        # self.i_a = Image.open(image_a).resize((256,256)).convert('RGB')
        # self.i_b = Image.open(image_b).resize((256,256)).convert('RGB')

        self.i_a = Image.open(image_a)
        self.i_b = Image.open(image_b)

        self.i_diff = image_diff

    def compare_images(self):
        h1 = self.i_a.histogram()
        h2 = self.i_b.histogram()
        return sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) for l, r in zip(h1, h2)) / len(h1)

    def output_diff(self):
        try:
            diff = ImageChops.difference(self.i_a, self.i_b)
            if diff.getbbox():
                PrintFormatUtil.print_line("存在差异, 生成差异图片 {}".format(self.i_diff))
                point_table = ([0] +([255] * 255))
                diff = diff.convert('L')
                diff = diff.point(point_table)
                new = diff.convert('RGB')
                new.paste(self.i_b, mask = diff)
                new.save(self.i_diff)
        except ValueError as e:
            text = ("表示图片大小和box对应的宽度不一致，参考API说明：Pastes another image into this image."
                    "The box argument is either a 2-tuple giving the upper left corner, a 4-tuple defining the left, upper, "
                    "right, and lower pixel coordinate, or None (same as (0, 0)). If a 4-tuple is given, the size of the pasted "
                    "image must match the size of the region.使用2纬的box避免上述问题")
            PrintFormatUtil.print_line("【{0}】{1}".format(e, text))
