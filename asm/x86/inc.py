from .x86_instruction import X86Instruction
from .x86_architecture import registers

class Inc(X86Instruction):

	def modifies_register(self, register):
		super().modifies_register(register)
		
		# if the argument is a register
		if self.arguments[0] == register:
			# it modifies the register
			return True
		else:
			return False

	@staticmethod
	def max_arguments(self):
		return 1

	@staticmethod
	def sets_zero_flag(self):
		return False