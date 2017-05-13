import asm.instruction
import asm.assembly
import sys

def decompile(filename):
	print('test')

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("No file specified")
		sys.exit()

	decompile(sys.argv[1])
