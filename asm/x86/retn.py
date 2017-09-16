from .x86_instruction import X86Instruction

class Retn(X86Instruction):

	@staticmethod
	def max_arguments(self):
		return 0

	@staticmethod
	def sets_zero_flag(self):
		return false