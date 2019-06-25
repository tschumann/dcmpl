from ..assembly import Assembly

from .instructions import get_instructions
from .x86_fpu_stack import X86FPUStack

class X86Assembly(Assembly):

	def __init__(self, raw_lines):
		super().__init__(raw_lines)
		self.fpu_stack = X86FPUStack()

	def get_valid_registers(self):
		if self.is_x64():
			return ['rax', 'rbx', 'rcx', 'rdx', 'rdi', 'rsi', 'rbp', 'rsp', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15']
		else:
			return ['eax', 'ebx', 'ecx', 'edx', 'edi', 'esi', 'ebp', 'esp']

	def get_valid_instructions(self):
		return get_instructions();

	def get_stack_register(self):
		if self.is_x64():
			return "rsp"
		else:
			return "esp"

	def is_x64(self):
		return False
