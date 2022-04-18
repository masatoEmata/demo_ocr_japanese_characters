import sys
import pyocr
from PIL import Image
import pyocr
import pyocr.builders


class ImgToTxtB:
    PATH_STR = rf'./input/img/message_sample.png'
    LAYOUT = 11
    LANG = 'script/Japanese'

    def __init__(self) -> None:
        tools = pyocr.get_available_tools()
        self.is_ocr_available(tools)
        self.tool = tools[0]

    def is_ocr_available(self, tools):
        if len(tools) == 0:
            print('Cannot use ocr tools.')
            sys.exit(1)

    def show_available_ocr_tools(self):
        names = self.tool.get_name()
        print(names)
        return names

    def show_available_languages(self):
        langs = self.tool.get_available_languages()
        print(langs)
        return langs
    
    def main(self):
        txt = self.tool.image_to_string(
            Image.open(self.PATH_STR), lang=self.LANG, builder=pyocr.builders.TextBuilder(tesseract_layout=self.LAYOUT)
        )
        print('\n\nOCR RESULT\n\n\n__________________\n\n',txt, '\n\n__________________\n\n')