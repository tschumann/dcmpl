from .x86_instruction import X86Instruction

class Mov(X86Instruction):

	@staticmethod
	def max_arguments(self):
		return 5

	@staticmethod
	def sets_zero_flag(self):
		return False

	def generate_code(self):
		# TODO: probably more complicated than this
		destination_index = 0
		source_index = 1

		# if the destination starts with "dword ptr"
		if self.arguments[destination_index] == "dword" and len(self.arguments) >= (destination_index + 2) and self.arguments[destination_index + 1] == "ptr":
			destination_index += 2
			# source will be a bit further along now
			source_index += 2

		# if the source starts with "dword ptr"
		if self.arguments[source_index] == "dword" and len(self.arguments) >= (source_index + 2) and self.arguments[source_index + 1] == "ptr":
			source_index += 2
		# if the source starts with "offset"
		elif self.arguments[source_index] == "offset":
			source_index += 1
		
		destination = self.arguments[destination_index]

		# if it's a local variable in the form [esp+XXh+var_X]
		if destination.startswith("[esp+"):
			# chop off the leading [esp+XXh+ and trailing ]
			# TODO: use a regex to make this not so hacky
			destination = destination[destination.rfind("+") + 1:-1]

		return [
			destination + " = " + self.arguments[source_index] + ";"
		]
