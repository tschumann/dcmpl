from ..instruction import Instruction
from .x86_architecture import registers
from abc import ABC, abstractmethod

class X86Instruction(Instruction, ABC):

	def modifies_register(self, register):
		# if it's not a valid register throw an error
		if register not in registers:
			raise ValueError("No such register " + register)

		return False

	@abstractmethod
	def max_arguments(self):
		pass
	
	@abstractmethod
	def sets_zero_flag(self):
		pass