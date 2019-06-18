import os
import sys
import unittest

# add the parent directory to the path (make it absolute to this works regardless of where it's called from)
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "..")

from asm.x86.mov import Mov

class TestX86Call(unittest.TestCase):

	def test_generate_code_simple(self):
		mov = Mov(['eax', 'ebx'])

		self.assertEqual(mov.generate_code(), ['eax = ebx;'])

	def test_generate_code_offset_src(self):
		mov = Mov(['[esp+10h+var_10]', 'offset', 'aPf_precache__5'])

		self.assertEqual(mov.generate_code(), ['var_10 = aPf_precache__5;'])

	def test_generate_code_dword_ptr_src(self):
		mov = Mov(['eax', 'dword', 'ptr', 'ds:(sv+30148h)[ebx*4]'])

		self.assertEqual(mov.generate_code(), ['eax = ds:(sv+30148h)[ebx*4];'])

	def test_generate_code_dword_ptr_dest(self):
		mov = Mov(['dword', 'ptr', 'ds:(sv+30948h)[ebx*4]', 'eax'])

		self.assertEqual(mov.generate_code(), ['ds:(sv+30948h)[ebx*4] = eax;'])

if __name__ == '__main__':
    unittest.main()
