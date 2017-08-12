from .x86_instruction import X86Instruction

class Jz(X86Instruction):

	@staticmethod
	def max_arguments(self):
		return 3

	@staticmethod
	def sets_zero_flag(self):
		return false