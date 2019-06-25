from .x86_instruction import X86Instruction

class Fsub(X86Instruction):

	def modifies_register(self, register):
		super().modifies_register(register)

		return False

	@staticmethod
	def max_arguments(self):
		return 2

	@staticmethod
	def sets_zero_flag(self):
		return False

	def uses_floating_point_stack(self):
		return True

	def generate_code(self):
		value = self.assembly.fpu_stack.pop()
		# TODO: add parentheses around this?
		self.assembly.fpu_stack.push(value + " - " + self.arguments[0])

		# code generation will happen in an instruction that pops the FPU stack
		return []
