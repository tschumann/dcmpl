from .x86_instruction import X86Instruction

class Test(X86Instruction):

	def modifies_register(self, register):
		super().modifies_register(register)
		
		return False

	@staticmethod
	def max_arguments(self):
		return 2

	@staticmethod
	def sets_zero_flag(self):
		return True

	def generate_code(self):
		# TODO: this needs to be an if statement probably
		return []