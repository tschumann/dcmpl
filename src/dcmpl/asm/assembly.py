import asm.x86.x86_instruction
import asm.x86.instructions

import re

# TODO: this should be a generic getter based on whatever CPU is currently being looked at
def get_x86_instructions():
	return asm.x86.instructions.get_instructions()

class Line(object):
	instruction = None
	arguments = []
	
class Assembly(object):
	lines = []
	registers = {}
	
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

	# TODO: eventuall get rid of this and move the processing into this class
	def get_lines(self):
		return self.lines