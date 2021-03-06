import os
import sys
import unittest

# add the parent directory to the path (make it absolute to this works regardless of where it's called from)
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "..")

from asm.x86.label import Label

class TestX86Label(unittest.TestCase):

	def test_generate_code(self):
		mov = Label(['loc_1234'])

		self.assertEqual(mov.generate_code(), ['loc_1234:'])

if __name__ == '__main__':
    unittest.main()
