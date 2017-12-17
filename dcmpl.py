import asm.instruction
import asm.assembly
import sys

def decompile(filename):
	raw_lines = []
	
	# get the assembly in line by line
	with open(filename) as file:
		raw_lines = file.read().splitlines()

	assembly = asm.assembly.Assembly(raw_lines)
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

				if instruction == "push":
					pass
				elif instruction == "pop":
					pass
				elif instruction == "inc":
					output_file.write(tokens[1] + "++;\n")
				elif instruction == "sub":
					# TODO: convert to decimal (or make leave as hex an option?) or convert to what C thinks hex is
					output_file.write(tokens[1] + " = " + tokens[1] + " - " + tokens[2] + ";\n")
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
	if len(sys.argv) < 2:
		print("No file specified")
		sys.exit()

	decompile(sys.argv[1])
