from abc import ABC, abstractmethod

class Instruction(object):
	arguments = []
	# whether this instruction has been processed for code generation in the scope of the parent assembly
	processed = False
	# keep track of the assembly this instruction is in - dirty but need the context of the whole assembly to generate decent code
	assembly = None
	# the index into the assembly's list of instructions
	assembly_index = -1

	def __init__(self, arguments):
		self.arguments = arguments
		self.processed = False
		self.assembly = None
		self.assembly_index = -1

	def generate_code(self):
		"""
		Generate C code for this instruction and its arguments.
		TODO: will probably need a reference to the global instruction list to be able to this
		"""
		raise Exception("Override generate_code in " + self.__class__.__name__)

	def modifies_register(self, register):
		# if it's not a valid register throw an error
		# TODO: this isn't the right place for this
		if register not in self.assembly.get_valid_registers():
			raise ValueError("No such register " + register)

		# let the subclasses figure it out
		return None

	def is_floating_point_instruction(self):
		return False

	def get_argument_count(self):
		return len(self.arguments)

	@abstractmethod
	def max_arguments(self):
		pass

	def is_processed(self):
		return self.processed

	def set_processed(self):
		self.processed = True
