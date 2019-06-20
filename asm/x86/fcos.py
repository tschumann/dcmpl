from .x86_instruction import X86Instruction

class Fcos(X86Instruction):

	def modifies_register(self, register):
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
		# argument to cos will be last thing pushed to FPU stack
		value = self.assembly.fpu_stack.pop()
		# put the result on top of the FPU stack
		self.assembly.fpu_stack.append("cos(" + value + ")")
		return []
