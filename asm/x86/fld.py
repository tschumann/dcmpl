from .x86_instruction import X86Instruction

class Fld(X86Instruction):

	def modifies_register(self, register):
		super().modifies_register(register)

		return False

	@staticmethod
	def max_arguments(self):
		return 3

	@staticmethod
	def sets_zero_flag(self):
		return False

	def uses_floating_point_stack(self):
		return True

	def generate_code(self):
		# put the value on the FPU stack
		# TODO: process it to strip off DWORD PTR etc
		self.assembly.fpu_stack.push(" ".join(self.arguments))

		# code generation will happen in an instruction that pops the FPU stack
		return []
