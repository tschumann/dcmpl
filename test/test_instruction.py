import os
import sys
import unittest

# add the parent directory to the path (make it absolute to this works regardless of where it's called from)
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "..")

from asm.instruction import Instruction

class TestInstruction(unittest.TestCase):

	def test_default_attributes(self):
		instruction = Instruction([])
		
		self.assertEqual(instruction.processed, False)
		self.assertEqual(instruction.assembly, None)
		self.assertEqual(instruction.assembly_index, -1)

if __name__ == '__main__':
    unittest.main()
