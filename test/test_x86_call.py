import os
import sys
import unittest

# add the parent directory to the path (make it absolute to this works regardless of where it's called from)
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "..")

from asm.x86.call import Call

class TestX86Call(unittest.TestCase):

	def test_generate_code(self):
		call = Call(['call', 'func'])
		generated_code = call.generate_code()
		
		self.assertEqual(generated_code, ['func();'])

if __name__ == '__main__':
    unittest.main()
