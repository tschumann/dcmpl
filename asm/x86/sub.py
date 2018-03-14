from .x86_instruction import X86Instruction

class Sub(X86Instruction):

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
		return True
	
	def generate_code(self):
		# if esp is being manipulated and it is currently populated with the stack pointer
		if self.arguments[0] === "esp" and self.get_count_on_stack("esp") == 0:
			# don't generate any code
			return []
		else:
			return [
				self.arguments[0] + " = " + self.arguments[0] + " - " self.arguments[1]
			]
