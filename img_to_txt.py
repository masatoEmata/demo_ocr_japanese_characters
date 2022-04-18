from PIL import Image
from pathlib import Path
import glob
import pyocr
import cv2


class ImageToTxt:
    PATH_PATTERN = './input/img/*.jpg'
    LAYOUT_RANGE = 13
    LANG = 'jpn'

    def __init__(self) -> None:
        tools = pyocr.get_available_tools()
        self.tesseract = tools[0]

    def open_img(self, path: Path):
        # img = Image.open(path)
        im_gray = cv2.imread(str(path), 0)
        path_gray = f'./input/img/img_gray/{path.name}'
        cv2.imwrite(path_gray, im_gray)
        img = Image.open(path_gray)
        return img

    def img_to_str(self, img: Image, tesseract_layout: int):
        print(f'METHOD NUMBER: {tesseract_layout}')
        try:
            txt = self.tesseract.image_to_string(
                img, lang=self.LANG, builder=pyocr.builders.TextBuilder(tesseract_layout=tesseract_layout)
            )
            print(f'TXT: {txt}')
        except Exception as e:
            print('NOT FOUND')

    def all_layout_img_to_str(self, img):
        for i in range(self.LAYOUT_RANGE):
            self.img_to_str(img, i)

    def all_img_to_str(self):
        for path_str in glob.glob(self.PATH_PATTERN):
            path = Path(path_str)
            print(f'FILE NAME: {path.name}')
            img = self.open_img(path)
            self.all_layout_img_to_str(img)


if __name__ == '__main__':
    i2t = ImageToTxt()
    i2t.all_img_to_str()