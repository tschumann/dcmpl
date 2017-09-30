from .x86_instruction import X86Instruction

class Mov(X86Instruction):

	@staticmethod
	def max_arguments(self):
		return 5

	@staticmethod
	def sets_zero_flag(self):
		return False