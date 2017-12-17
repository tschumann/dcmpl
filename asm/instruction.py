from abc import ABC, abstractmethod

class Instruction(object):
	arguments = []
	# whether this instruction has been processed for code
	# generation in the scope of the parent assembly
	processed = False
	# keep track of the assembly this instruction is in - dirty but
	#  need the context of the whole assembly to generate decent code 
	assembly = None
	# the index into the assembly's list of instructions
	assembly_index = -1

	def __init__(self, arguments):
		self.arguments = arguments
		self.processed = False
		self.assembly = None
		self.assembly_index = -1

	@abstractmethod
	def generate_code(self):
		"""
		Generate C code for this instruction and its arguments.
		TODO: will probably need a reference to the global instruction list to be able to this
		TODO: need to fail if processed is True
		"""

	@abstractmethod
	def modifies_register(self, register):
		pass

	@abstractmethod
	def max_arguments(self):
		pass
