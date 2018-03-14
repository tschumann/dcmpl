import asm.instruction
import asm.assembly
import asm.mips.mips_assembly
import asm.x86.x86_assembly
import sys

def decompile(architecture, filename):
	raw_lines = []
	
	# get the assembly in line by line
	with open(filename) as file:
		raw_lines = file.read().splitlines()

	if architecture == 'x86':
		assembly = asm.x86.x86_assembly.X86Assembly(raw_lines)
	elif architecture == 'mips':
		assembly = asm.mips.mips_assembly.MIPSAssembly(raw_lines)
	else:
		# TODO: error out
		assembly = None

	cleaned_lines = assembly.get_lines()
			
	output_file = open(filename + ".c", "w")

	for line in cleaned_lines:
		tokens = line
		for index in range(0, len(line)):
			instruction = tokens[0]

			# if it's the first token then it could be an instruction
			# if it doesn't end with a : (like a label) then it is an instruction
			if index == 0 and instruction[-1:] != ":":
				
				# TODO: need to work out something better - the token may not be a valid instruction and if it is we want to know so we can support it - shouldn't get this far if it's not a valid instruction though
				if assembly.is_valid_instruction(instruction):
					# instantiate the instruction class with the instruction parameters and generate the code
					generated_code = assembly.get_instruction_class_object(instruction, tokens[1:]).generate_code()

					for line in generated_code:
						output_file.write(line  + "\n");
				else:
					print("Unknown instruction " + instruction)

				if instruction == "inc":
					output_file.write(tokens[1] + "++;\n")
				elif instruction == "mov":
					if tokens[2] == "offset":
						output_file.write(tokens[1] + " = &" + tokens[3] + ";\n")
					elif tokens[1] == "dword" and len(tokens) > 3 and tokens[2] == "ptr":
						output_file.write(tokens[3] + " = " + tokens[4] + ";\n")
					else:
						output_file.write(tokens[1] + " = " + tokens[2] + ";\n")
					continue
			# if it is a label
			elif index == 0 and instruction[-1:] == ":":
				output_file.write(instruction + "\n")

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print("No architecture and file specified")
		sys.exit()

	decompile(sys.argv[1], sys.argv[2])
