from .x86_instruction import X86Instruction

class Test(X86Instruction):

	@staticmethod
	def max_arguments(self):
		return 2

	@staticmethod
	def sets_zero_flag(self):
		return true