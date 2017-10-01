import asm.x86.x86_instruction
import asm.x86.instructions

import re

# TODO: this should be a generic getter based on whatever CPU is currently being looked at
def get_x86_instructions():
	return asm.x86.instructions.get_instructions()
	
class Assembly(object):
	lines = []
	registers = {}
	instructions = []
	stack = []
	
	def __init__(self, raw_lines):
		lines = []

		# tidy up the raw assembly
		for line in raw_lines:
			tokens = line.split()
			cleaned_line = []

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
					
				cleaned_line.append(token)
				
			# if there was actually something we can use on the line, keep it
			if len(cleaned_line) > 0:
				lines.append(cleaned_line)
			
		self.lines = lines

		valid_instructions = get_x86_instructions()

		for tokens in self.lines:
			instruction_name = tokens[0]

			# if the instruction is known
			if instruction_name in valid_instructions:
				# instantiate an instance of the instruction with the arguments
				instruction = valid_instructions[instruction_name](tokens[1:])
				# add it to the list of instructions
				self.instructions.append(instruction)
	
	def generate_code(self):
		for instruction in self.instructions:
			instruction.generate_code()

	# TODO: eventuall get rid of this and move the processing into this class
	def get_lines(self):
		return self.lines