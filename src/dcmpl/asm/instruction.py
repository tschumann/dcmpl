
class Instruction(object):
	arguments = []
	processed = False

	def __init__(self, arguments):
		self.arguments = arguments
		self.processed = False

	def generate_code(self):
		"""
		Generate C code for this instruction and its arguments.
		TODO: will probably need a reference to the global instruction list to be able to this
		"""
		pass
