import sys
import pyocr

from PIL import Image
import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()

#OCRが使えるかチェック
if len(tools) == 0:
    print('OCRツールが使えません')
    sys.exit(1)

tool = tools[0]
print("インストールされているOCRツールは', %s" % (tool.get_name()) ,'です。\n Tesseract（テッセラクト）は光学文字認識のエンジンです。\n\n') 

langs = tool.get_available_languages()
print(langs,'などの言語を指定できます。')

# OCRを実行する画像イメージや言語指定、オプション指定
txt = tool.image_to_string( 
    Image.open(rf"./input/img/message_sample.png"),  # ここを変更
    lang='script/Japanese',
    builder=pyocr.builders.TextBuilder(tesseract_layout=11) #オプション番号は必要に応じて変更してください。デフォルトは「3」
)
print('\n\nOCR（光学文字認識）の実行結果\n\n\n__________________\n\n',txt, '\n\n__________________\n\n')