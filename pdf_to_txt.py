# Credit: https://gammasoft.jp/blog/python-parse-pdf-contents/

import sys
from pathlib import Path
from subprocess import call
import glob

cmd_input = 'cd ./input/pdf/'
cmd_output = 'cd ./output/pdf/'
cmd_root = 'cd ../..'
cmd_move = 'move *.txt ./output/txt'
 
py_path = Path(sys.exec_prefix) / "Scripts" / "pdf2txt.py"
for x in glob.glob("./input/pdf/*.pdf"):
    path = Path(x)
    call(cmd_output.split(), shell=True)
    result = call(["py", str(py_path), f"-o {path.stem}.txt", "-p 1", path])
    print(path)
    call(cmd_root.split(), shell=True)
    call(cmd_move.split(), shell=True)