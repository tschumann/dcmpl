from ..assembly import Assembly

from .instructions import get_instructions

class X86Assembly(Assembly):

	def __init__(self, raw_lines):
		super().__init__(raw_lines)

		# TODO: work out how to deal with x86/x64
		if True:
			self._valid_registers = ['eax', 'ebx', 'ecx', 'edx', 'edi', 'esi', 'edp', 'esp']
		else:
			self._valid_registers = ['rax', 'rbx', 'rcx', 'rdx', 'rdi', 'rsi', 'rbp', 'rsp', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15']

		# cache this as a member
		self._valid_instructions = get_instructions()
