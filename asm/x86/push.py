from .x86_instruction import X86Instruction

class Push(X86Instruction):

	def modifies_register(self, register):
		super().modifies_register(register)

		# pushing to the stack modifies the stack pointer
		if register == 'esp':
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
		# keep track of the push
		self.assembly.stack.append(self.arguments[0])
