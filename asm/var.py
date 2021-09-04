from .instruction import Instruction

class Var(Instruction):
	"""
	Not an instruction but covers IDA's arg_ and var_ declarations.
	"""

	def modifies_register(self, register):
		super().modifies_register(register)
		
		return False

	@staticmethod
	def max_arguments(self):
		return 4

	@staticmethod
	def sets_zero_flag(self):
		return False

	def generate_code(self):
		return [
			"void *" + self.arguments[0]
		]