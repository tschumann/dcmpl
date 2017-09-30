import os
import sys
import unittest

# add the parent directory to the path (make it absolute to this works regardless of where it's called from)
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "..")

from asm.x86.call import Call
from asm.x86.x86_architecture import registers

class TestX86Call(unittest.TestCase):

	def test_modifies_register(self):
		provider = [
			['eax', True],
			['ebx', False],
			['ecx', False],
			['edx', False],
			['edi', False],
			['esi', False],
			['esp', False]
		]
		# make sure all registers are being checked
		self.assertEqual(len(provider), len(registers))

		call = Call(['call', 'func'])

		for e in provider:
			self.assertEqual(call.modifies_register(e[0]), e[1])

	def test_generate_code(self):
		call = Call(['call', 'func'])
		
		self.assertEqual(call.generate_code(), ['func();'])

if __name__ == '__main__':
    unittest.main()
