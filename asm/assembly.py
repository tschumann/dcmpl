import re
import pathlib

from typing import List
	
class Assembly(object):

	def __init__(self, raw_lines: List[str]):
		# our representation of instructions
		self.instructions = []
		# register stack
		self.stack = []
		# state of the stacks etc at jump instructions
		self.label_contexts = {}
		# lines of generated code
		self.output = []

		valid_instructions = []

		lines = []

		# cache this
		valid_instructions = self.get_valid_instructions()

		line_number = 1

		# tidy up the raw assembly
		for line in raw_lines:
			tokens = line.split()
			cleaned_line = []

			# look at each token
			for token in tokens:
				# if this token starts a comment, skip everything after it
				if token[0] == ";":
					break
					
				# if the token looks like .segm:DEADBEEF skip it as it's IDA-specific extra stuff
				if re.match("\\.\\w+:\\d+", token):
					continue

				# if the token ends with a comma, strip off the comma
				if token[-1:] == ",":
					token = token[:-1]

				# add the cleaned up token to the current line
				cleaned_line.append(token)

			# if there was actually something we can use on the line, keep it
			if len(cleaned_line) > 0:
				lines.append({"cleaned_line": cleaned_line, "line_number": line_number})

			line_number += 1

		# turn the cleaned up assembly into instruction classes
		for line in lines:
			tokens = line["cleaned_line"]
			instruction_name = tokens[0]
			instruction_arguments = tokens[1:]
			instruction = None

			# if the instruction is known
			if instruction_name in valid_instructions:
				# instantiate an instance of the instruction with the arguments
				instruction = valid_instructions[instruction_name](instruction_arguments)
			# if it's not known but it looks like a label
			elif instruction_name[-1:] == ":":
				# instantiate a label instruction
				instruction = valid_instructions["label"]([instruction_name[:-1]])
			# if it's an IDA function argument or local parameter
			elif instruction_name.startswith("arg_") or instruction_name.startswith("var_"):
				# instantiate a label instruction
				print(instruction_arguments)
				instruction = valid_instructions["var"]([instruction_name] + instruction_arguments)
			# if it's func_name proc near or func_name endp then skip it
			elif len(instruction_arguments) > 0 and instruction_arguments[0] in ["proc", "endp"]:
				continue
			else:
				print("Unknown instruction " + instruction_name)

			if instruction:
				instruction.assembly = self
				instruction.line_number = line["line_number"]
				instruction.assembly_index = len(self.instructions)
				# add it to the list of instructions
				self.instructions.append(instruction)

	def process_instructions(self):
		for instruction in self.instructions:
			pass

	def generate_code(self):
		for instruction in self.instructions:
			if instruction.is_processed():
				raise Exception("Instruction has already been processed!")
			if not instruction.should_generate_code:
				continue
			else:
				generated_code = instruction.generate_code()

				if generated_code is not None and len(generated_code) > 0:
					self.output.extend(generated_code)
					instruction.set_processed()

	def write_code_to_file(self, output_filename: str):
		output_filename = pathlib.Path(output_filename).stem + ".c"
		print("Writing to " + output_filename)
		output_file = open(output_filename, "w")

		for line in self.output:
			output_file.write(line + "\n");

	def get_valid_registers(self):
		# offload this to subclasses
		pass

	def get_valid_instructions(self):
		# offload this to subclasses
		pass

	def get_stack_register(self):
		# offload this to subclasses
		pass

	def get_count_on_stack(self, register: str):
		"""
		Get the number of times the given register is currently pushed on the stack.
		"""
		count = 0

		for stored in self.stack:
			if stored == register:
				count += 1

		return count
