class X86FPUStack:

	fpu_stack = []

	def push(self, value):
		self.fpu_stack.append(value)

	def pop(self):
		return self.fpu_stack.pop()
