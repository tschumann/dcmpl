import asm.instruction
import asm.assembly
import re
import sys

def decompile(filename):
	raw_lines = []
	cleaned_lines = []
	
	with open(filename) as file:
		raw_lines = file.read().splitlines()
		
	for line in raw_lines:
		tokens = line.split()
		cleaned_line = []

		for token in tokens:
			# skip comments
			if token[0] == ";":
				continue
				
			if re.match("\\.\\w+:\\d+", token):
				continue

			if token[-1:] == ",":
				token = token[:-1]
				
			cleaned_line.append(token)
			
		if len(cleaned_line) > 0:
			cleaned_lines.append(cleaned_line)
			
	output_file = open(filename + ".c", "w")
	
	# TODO: eventually make this per-CPU
	instructions = asm.assembly.get_x86_instructions()
			
	for line in cleaned_lines:
		tokens = line
		for index in range(0, len(line)):
			# if it's the first token then it could be an instruction
			# if it doesn't end with a : (like a label) then it is an instruction
			if index == 0 and tokens[0][-1:] != ":":
				instruction = None
				
				# TODO: need to work out something better - the token may not be a valid instruction and if it is we want to know so we can support it
				if tokens[0] in instructions:
					instruction = instructions[tokens[0]]

				if tokens[0] == "push":
					pass
				elif tokens[0] == "pop":
					pass
				elif tokens[0] == "retn":
					output_file.write("return;\n")
				elif tokens[0] == "mov":
					if tokens[2] == "offset":
						output_file.write(tokens[1] + " = &" + tokens[3] + ";\n")
					elif tokens[1] == "dword" and len(tokens) > 3 and tokens[2] == "ptr":
						output_file.write(tokens[3] + " = " + tokens[4] + ";\n")
					else:
						output_file.write(tokens[1] + " = " + tokens[2] + ";\n")
					continue
				else:
					if len(tokens) >= 2 and tokens[1] == "proc":
						output_file.write("void *" + tokens[0] + "()\n")
			elif index == 0 and tokens[0][-1:] == ":":
				output_file.write(tokens[0] + "\n")

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("No file specified")
		sys.exit()

	decompile(sys.argv[1])
