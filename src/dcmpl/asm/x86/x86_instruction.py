from ..instruction import Instruction
from abc import ABC, abstractmethod

class X86Instruction(Instruction, ABC):

	@abstractmethod
	def max_arguments(self):
		pass
	
	@abstractmethod
	def sets_zero_flag(self):
		pass