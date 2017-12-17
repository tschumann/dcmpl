from .x86_instruction import X86Instruction

class Align(X86Instruction):
	"""
	Not really an instruction but IDA outputs this.
	"""

	def modifies_register(self, register):
		super().modifies_register(register)
		
		return False

	@staticmethod
	def max_arguments(self):
		return 1

	@staticmethod
	def sets_zero_flag(self):
		return False

	def generate_code(self):
		return []
