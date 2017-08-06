from .x86_instruction import X86Instruction

class Retn(X86Instruction):

	def max_arguments(self):
		return 0

	def sets_zero_flag(self):
		return false