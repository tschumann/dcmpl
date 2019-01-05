import re
	
class Assembly(object):
	# input lines
	lines = []
	# our representation of instructions
	instructions = []
	# register stack
	stack = []

	output = []

	_valid_instructions = []

	def __init__(self, raw_lines):
		lines = []

		self._valid_instructions = self.get_valid_instructions()

		# tidy up the raw assembly
		for line in raw_lines:
			tokens = line.split()
			cleaned_line = []

			# look at each token
			for token in tokens:
				# if this token starts a comment, skip everything after it
				if token[0] == ";":
					break
					
				# if the token looks like .segm:DEADBEEF skip
				# it as it's IDA-specific extra stuff
				if re.match("\\.\\w+:\\d+", token):
					continue

				# if the token ends with a comma, strip off the comma
				if token[-1:] == ",":
					token = token[:-1]

				# save the line after getting rid of bad tokens etc
				cleaned_line.append(token)

			# if there was actually something we can use on the line, keep it
			if len(cleaned_line) > 0:
				lines.append(cleaned_line)
			
		self.lines = lines

		# turn the processed assembly into instruction classes
		for tokens in self.lines:
			instruction_name = tokens[0]

			# if the instruction is known
			if instruction_name in self._valid_instructions:
				# instantiate an instance of the instruction with the arguments
				instruction = self._valid_instructions[instruction_name](tokens[1:])
				# add it to the list of instructions
				self.instructions.append(instruction)
			# if it looks like a label
			elif instruction_name[-1:] == ":":
				# instantiate a label instruction
				instruction = self._valid_instructions["label"]([instruction_name[:-1]])
				# add it to the list of instructions
				self.instructions.append(instruction)
			else:
				print("Unknown instruction " + instruction_name)

	def is_valid_instruction(self, instruction):
		if instruction in self._valid_instructions:
			return True
		else:
			# TODO: handle functions and labels etc
			# TODO: to do that, turn this into an object from instruction method?
			return False

	def get_instruction_class_object(self, instruction, arguments):
		# get the instruction class
		instruction_class = self._valid_instructions[instruction]
		# instantiate the instruction class with the instruction parameters
		return instruction_class(arguments)
	
	def generate_code(self, output_filename):
		for instruction in self.instructions:
			self.output.extend(instruction.generate_code())
			instruction.set_processed()

		output_file = open(output_filename + ".c", "w")

		for line in self.output:
			output_file.write(line + "\n");

	# TODO: eventually get rid of this and move the processing into this class
	def get_lines(self):
		return self.lines

	def get_valid_registers(self):
		pass

	def get_valid_instructions(self):
		pass

	def get_stack_register(self):
		pass