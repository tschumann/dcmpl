from .x86_instruction import X86Instruction

class Retn(X86Instruction):

	def modifies_register(self, register):
		super().modifies_register(register)
		
		# TODO: not always False (complicated)
		return False

	@staticmethod
	def max_arguments(self):
		return 0

	@staticmethod
	def sets_zero_flag(self):
		return False

	def generate_code(self):
		# TODO: this needs to be an if statement probably
		return [
			"return;"
		]