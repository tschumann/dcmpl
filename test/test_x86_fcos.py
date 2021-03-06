import os
import sys
import unittest

# add the parent directory to the path (make it absolute to this works regardless of where it's called from)
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "..")

from asm.x86.x86_assembly import X86Assembly
from asm.x86.fcos import Fcos
from asm.x86.fld import Fld
from asm.x86.fstp import Fstp

class TestX86Fcos(unittest.TestCase):

	def test_generate_code(self):
		assembly = X86Assembly([])

		fld = Fld(['DWORD PTR [esp+4]'])
		fld.assembly = assembly
		fcos = Fcos([])
		fcos.assembly = assembly
		fstp = Fstp(['[esp+7Ch+var_3C]'])
		fstp.assembly = assembly
		
		fld.generate_code()
		fcos.generate_code()
		fstp.generate_code()
		
		self.assertEqual(fld.generate_code(), [])
		self.assertEqual(fcos.generate_code(), [])
		self.assertEqual(fstp.generate_code(), ['[esp+7Ch+var_3C] = cos(DWORD PTR [esp+4]);'])

if __name__ == '__main__':
    unittest.main()
