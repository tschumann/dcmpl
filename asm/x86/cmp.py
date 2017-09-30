from .x86_instruction import X86Instruction

class Cmp(X86Instruction):

	def modifies_register(self, register):
		super().modifies_register(register)
		
		return False

	@staticmethod
	def max_arguments(self):
		return 5

	@staticmethod
	def sets_zero_flag(self):
		return True