import sys
import unittest

# deal with the confusing insanity of Python's import rules
# TODO: hacky - use full path relative to this file?
sys.path.append('..')

from asm.x86.call import Call

class TestX86Call(unittest.TestCase):

	def test_generate_code(self):
		call = Call(['call', 'func'])
		generated_code = call.generate_code()
		
		self.assertEqual(generated_code, ['func();'])

if __name__ == '__main__':
    unittest.main()
