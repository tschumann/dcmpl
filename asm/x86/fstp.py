from .x86_instruction import X86Instruction

class Fstp(X86Instruction):

	def modifies_register(self, register):
		super().modifies_register(register)

		return False

	@staticmethod
	def max_arguments(self):
		return 1

	@staticmethod
	def sets_zero_flag(self):
		return False

	def uses_floating_point_stack(self):
		return True

	def generate_code(self):
		# get the index of the previous instruction
		index = self.assembly_index - 1

		while True:
			previous_instruction = self.assembly.instructions[index]

			if len(self.assembly.fpu_stack) == 0 or index == 0:
				return

			if not previous_instruction.is_processed() and previous_instruction.uses_floating_point_stack():
				pass

			index -= 1

		return []
