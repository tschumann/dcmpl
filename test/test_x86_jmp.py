import os
import sys
import unittest

# add the parent directory to the path (make it absolute to this works regardless of where it's called from)
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "..")

from asm.x86.jmp import Jmp

class TestX86Jmp(unittest.TestCase):

	def test_generate_code_single_argument(self):
		mov = Jmp(['loc_1234'])

		self.assertEqual(mov.generate_code(), ['goto loc_1234;'])

	def test_generate_code_short_argument(self):
		mov = Jmp(['short', 'loc_1234'])

		self.assertEqual(mov.generate_code(), ['goto loc_1234;'])

if __name__ == '__main__':
    unittest.main()
