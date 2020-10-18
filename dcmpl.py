import asm.instruction
import asm.assembly
import asm.mips.mips_assembly
import asm.x86.x86_assembly
import sys

def decompile(architecture, filename: str):
	raw_lines = []
	
	# get the assembly in line by line
	with open(filename) as file:
		raw_lines = file.read().splitlines()

	if architecture == 'x86':
		assembly = asm.x86.x86_assembly.X86Assembly(raw_lines)
	elif architecture == 'mips':
		assembly = asm.mips.mips_assembly.MIPSAssembly(raw_lines)
	else:
		print("Unknown architecture " + architecture)

		return

	assembly.generate_code(filename)

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print("No architecture and file specified")
		sys.exit()

	decompile(sys.argv[1], sys.argv[2])
