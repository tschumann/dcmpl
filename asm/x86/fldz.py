from .x86_instruction import X86Instruction

class Fldz(X86Instruction):

	def modifies_register(self, register):
		super().modifies_register(register)

		return False

	@staticmethod
	def max_arguments(self):
		return 0

	@staticmethod
	def sets_zero_flag(self):
		return False

	def uses_floating_point_stack(self):
		return True

	def generate_code(self):
		# put 0.0 on the FPU stack
		self.assembly.fpu_stack.append("0.0")

		# code generation will happen in an instruction that pops the FPU stack
		return []
