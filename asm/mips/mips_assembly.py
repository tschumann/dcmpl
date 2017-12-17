from ..assembly import Assembly

from .instructions import get_instructions

class MIPSAssembly(Assembly):

	def __init__(self, raw_lines):
		super().__init__(raw_lines)

		self._valid_registers = ['a0', 'a1', 'a2', 'a3', 't0', 't1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't8', 't9', 's0', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 'v0', 'v1', 'sp', 'fp', 'gp', 'ra']

		# cache this as a member
		self._valid_instructions = get_instructions()
