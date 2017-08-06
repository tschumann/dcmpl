from .x86_instruction import X86Instruction

class Test(X86Instruction):

	def max_arguments(self):
		return 2

	def sets_zero_flag(self):
		return true