from .x86_instruction import X86Instruction

class Label(X86Instruction):
	"""
	Not really an instruction need a way to represent a jump destination.
	"""

	def modifies_register(self, register):
		super().modifies_register(register)
		
		return False

	@staticmethod
	def max_arguments(self):
		return 0

	@staticmethod
	def sets_zero_flag(self):
		return False

	def generate_code(self):
		return [
			self.arguments[0] + ":"
		]
