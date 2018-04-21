import os
import sys
import unittest

# add the parent directory to the path (make it absolute to this works regardless of where it's called from)
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "..")

from asm.x86.x86_assembly import X86Assembly
from asm.x86.call import Call

class TestX86Call(unittest.TestCase):

	def test_modifies_register(self):
		assembly = X86Assembly([])

		provider = [
			['eax', True],
			['ebx', False],
			['ecx', False],
			['edx', False],
			['edi', False],
			['esi', False],
			['ebp', False],
			['esp', False]
		]
		# make sure all registers are being checked
		self.assertEqual(len(provider), len(assembly.get_valid_registers()))

		call = Call(['func'])
		call.assembly = assembly

		for e in provider:
			self.assertEqual(call.modifies_register(e[0]), e[1])

	def test_generate_code(self):
		call = Call(['func'])
		
		self.assertEqual(call.generate_code(), ['eax = func();'])

if __name__ == '__main__':
    unittest.main()
