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

	# TODO: in code generation push FPU state (and other state? regular register stack too probably)
	# and store it against the label that is being jumped to so that code generation at the point of
	# the label has the correct context
	# NOTE: store label+line number as a label could be jumped to from multiple locations
