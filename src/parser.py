import argparse
import re


patterns = [
	r'(mov)\s+(\w+),\s+(\d+)',
	r'(mov)\s+(0x\d+),\s+(\w+)',
	r'(add)\s+(\w+),\s+(\w+)',
	r'(inc)\s+(0x\d+)',
	r'(imul)\s+(\w+),\s+(0x\d+),\s+(\d+)'
]

parser = argparse.ArgumentParser(description='Lê comandos assembly de arquivo')
parser.add_argument('--path', help='Recebe caminho absoluto para o arquivo de texto', type=argparse.FileType('r'))

args = parser.parse_args()

for line in args.path.readlines():
	for pattern in patterns:
		matched = re.match(pattern, line)
		if matched:
			btArr = bytearray(str(matched.groups()), encoding='utf-8')
			print('encoded: ', btArr)
			print('decoded: ', btArr.decode('utf-8', errors='ignore'))
		print(matched.groups() if matched else None)
