import asm.x86.x86_instruction
import asm.x86.instructions

import re
	
class Assembly(object):
	lines = []
	registers = {}
	instructions = []
	stack = []
	
	_valid_instructions = []

	def __init__(self, raw_lines):
		lines = []

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

			# if it's a function, swap things around so it's handled as an instruction
			if len(cleaned_line) > 1 and cleaned_line[1] == "proc":
				function_name = cleaned_line[0]
				cleaned_line[0] = "proc"
				cleaned_line[1] = function_name

			# if there was actually something we can use on the line, keep it
			if len(cleaned_line) > 0:
				lines.append(cleaned_line)
			
		self.lines = lines

		self._valid_instructions = asm.x86.instructions.get_instructions()

		for tokens in self.lines:
			instruction_name = tokens[0]

			# if the instruction is known
			if instruction_name in self._valid_instructions:
				# instantiate an instance of the instruction with the arguments
				instruction = self._valid_instructions[instruction_name](tokens[1:])
				# add it to the list of instructions
				self.instructions.append(instruction)

	def is_valid_instruction(self, instruction):
		if instruction in self._valid_instructions:
			return True
		else:
			# TODO: handle functions and labels etc
			return False

	def get_instruction_class_object(self, instruction, arguments):
		# get the instruction class
		instruction_class = self._valid_instructions[instruction]
		# instantiate the instruction class with the instruction parameters
		return instruction_class(arguments)
	
	def generate_code(self):
		for instruction in self.instructions:
			instruction.generate_code()

	# TODO: eventuall get rid of this and move the processing into this class
	def get_lines(self):
		return self.lines
