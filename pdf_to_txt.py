
import sys
from pathlib import Path
from subprocess import call
import glob


PAGE_NUM = 1

def invoke_converter(path_str):
    path = Path(path_str)
    py_path = Path(sys.exec_prefix) / "Scripts" / "pdf2txt.py"
    call(["py", str(py_path), f"-o {path.stem}.txt", f"-p {PAGE_NUM}", path])

def move_to_output_dir():
    cmd = 'cd ./output/pdf/'
    call(cmd.split(), shell=True)

def move_to_root_dir():
    cmd = 'cd ../..'
    call(cmd.split(), shell=True)

def move_output_files():
    cmd = 'move *.txt ./output/txt'
    call(cmd.split(), shell=True)

for path_str in glob.glob("./input/pdf/*.pdf"):
    move_to_output_dir()
    invoke_converter(path_str)
    move_to_root_dir()
    move_output_files()


# Based on: https://gammasoft.jp/blog/python-parse-pdf-contents/