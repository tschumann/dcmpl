from ..assembly import Assembly

from .instructions import get_instructions

class MIPSAssembly(Assembly):

	def get_valid_registers(self):
		return ['a0', 'a1', 'a2', 'a3', 't0', 't1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't8', 't9', 's0', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 'v0', 'v1', 'sp', 'fp', 'gp', 'ra']

	def get_valid_instructions(self):
		return get_instructions();
