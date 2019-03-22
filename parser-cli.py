from src.read_write import ReadWrite
from config import _arch
import argparse
import re

patterns = [
    r'(mov)\s*(\w+),\s*(\w+)',
    r'(add)\s*(\w+),\s*(\w+)',
    r'(inc)\s*(\w+)',
    r'(imul)\s*(\w+),\s*(\w+),\s*(\w+)',
    r'(imul)\s*(\w+),\s*(\w+)'
]

parser = argparse.ArgumentParser(description='Lê comandos assembly de arquivo')
parser.add_argument('--path',
                    help='Recebe caminho absoluto para o arquivo de texto',
                    type=argparse.FileType('r'))
parser.add_argument('--command',
                    help='Recebe comando direto do terminal')

args = parser.parse_args()

if args.command:
    for pattern in patterns:
        matched = re.match(pattern, args.command)
        if matched:
            print('\n', matched.groups())
            btArr = bytearray(str(matched.groups()), encoding='utf-8')
            print('encoded: ', btArr)
            print('decoded: ', btArr.decode('utf-8', errors='ignore'), '\n')
            rw = ReadWrite()
            rw.save_instruction(btArr, size=_arch)

elif args.path:
    for line in args.path.readlines():
        for pattern in patterns:
            matched = re.match(pattern, line)
            if matched:
                print('\n', matched.groups())
                btArr = bytearray(str(matched.groups()), encoding='utf-8')
                print('encoded: ', btArr)
                print('decoded: ', btArr.decode('utf-8', errors='ignore'))
                rw = ReadWrite()
                rw.save_instruction(btArr, size=_arch)
