from .x86_instruction import X86Instruction

class Pop(X86Instruction):

	@staticmethod
	def max_arguments(self):
		return 1

	@staticmethod
	def sets_zero_flag(self):
		return false