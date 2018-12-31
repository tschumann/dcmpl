from .x86_instruction import X86Instruction

class Jmp(X86Instruction):

	def modifies_register(self, register):
		super().modifies_register(register)
		
		return False

	@staticmethod
	def max_arguments(self):
		return 2

	@staticmethod
	def sets_zero_flag(self):
		return False

	def generate_code(self):
		label = self.arguments[0]

		if self.get_argument_count() == 2 and self.arguments[0] == "short":
			label = self.arguments[1]

		return [
			"goto " + label + ";"
		]
