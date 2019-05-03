from src.read_write import ReadWrite
from config import get_bus_size, get_arch
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
            for p in matched.groups():
                print('Palavra maior que o tamanho do barramento') if \
                    len(p) > get_bus_size() else None
            bytes_list = [x.encode('utf-8') for x in matched.groups()]
            print('\n', matched.groups())
            print('encoded: ', bytes_list)
            rw = ReadWrite()
            rw.save_instruction(bytes_list)

elif args.path:
    for line in args.path.readlines():
        for pattern in patterns:
            matched = re.match(pattern, line)
            if matched:
                for p in matched.groups():
                    print('Palavra maior que o tamanho do barramento') if \
                        len(p) > get_bus_size() else None
                bytes_list = [x.encode('utf-8') for x in matched.groups()]
                print('\n', matched.groups())
                print('encoded: ', bytes_list)
                rw = ReadWrite()
                rw.save_instruction(bytes_list)
