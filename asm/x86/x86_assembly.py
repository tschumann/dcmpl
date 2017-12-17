from ..assembly import Assembly

from .instructions import get_instructions

class X86Assembly(Assembly):

	def get_valid_registers(self):
		if self.is_x64():
			return ['rax', 'rbx', 'rcx', 'rdx', 'rdi', 'rsi', 'rbp', 'rsp', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15']
		else:
			return ['eax', 'ebx', 'ecx', 'edx', 'edi', 'esi', 'ebp', 'esp']

	def get_valid_instructions(self):
		return get_instructions();

	def is_x64(self):
		return False
