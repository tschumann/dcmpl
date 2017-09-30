from .x86_instruction import X86Instruction

class Jz(X86Instruction):

	def modifies_register(self, register):
		super().modifies_register(register)
		
		return False

	@staticmethod
	def max_arguments(self):
		return 3

	@staticmethod
	def sets_zero_flag(self):
		return False