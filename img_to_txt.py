from PIL import Image
from pathlib import Path
import glob

import pyocr
import cv2

tools = pyocr.get_available_tools()
tesseract = tools[0]
# print(tools)


# PDFファイルのパスを取得し順番に捌いていく
for x in glob.glob("./input/img/*sample_2.jpg"):
    path = Path(x)
    # img = Image.open(path)
    im_gray = cv2.imread(str(path), 0)
    path_gray = f'./input/img/img_gray/{path.name}'
    cv2.imwrite(path_gray, im_gray)
    img = Image.open(path_gray)

    # img.show()
    for i in range(13):
        print('######################')
        print(f'METHOD NUMBER: {i}')
        try:
            txt = tesseract.image_to_string(
                img, lang='jpn', builder=pyocr.builders.TextBuilder(tesseract_layout=i)
            )
            print(f'FILE NAME: {path.name}')
            print(f'TXT: {txt}')
        except Exception as e:
            print('NOT FOUND')
        print('######################')