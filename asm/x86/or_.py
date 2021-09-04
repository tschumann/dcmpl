from .x86_instruction import X86Instruction

class Or(X86Instruction):

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
		return 2

	@staticmethod
	def sets_zero_flag(self):
		return False

	def generate_code(self):
		return [
			self.arguments[0] + " = " + self.arguments[0] + " | " + self.arguments[1] + ";"
		]
