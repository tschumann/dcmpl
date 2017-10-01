from .x86_instruction import X86Instruction
from .x86_architecture import registers

class Pop(X86Instruction):

	def generate_code(self):
		self.assembly.stack.pop()

	def modifies_register(self, register):
		super().modifies_register(register)

		# popping modifies the target register and the stack pointer
		if self.arguments[0] == register or register == 'esp':
			return True
		else:
			return False

	@staticmethod
	def max_arguments(self):
		return 1

	@staticmethod
	def sets_zero_flag(self):
		return False