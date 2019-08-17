class X86FPUStack:
	"""
	x86 FPU stack to keep track of values that get pushed/popped by floating point operations.
	Uses an array as a stack by pretending that the last element in the array is the top of the stack.
	"""

	fpu_stack = []

	def push(self, value):
		self.fpu_stack.append(value)

	def pop(self):
		return self.fpu_stack.pop()

	def peek(self):
		return self.fpu_stack[-1]