from .x86_instruction import X86Instruction

class Call(X86Instruction):

	def modifies_register(self, register):
		super().modifies_register(register)
		
		# TODO: does it touch esp? retn does but should we consider this does too?
		if register == 'eax':
			return True
		else:
			return False

	@staticmethod
	def max_arguments(self):
		return 1

	@staticmethod
	def sets_zero_flag(self):
		return False

	def generate_code(self):
		# TODO: need to find likely arguments
		return [
			self.arguments[1] + "();"
		]
