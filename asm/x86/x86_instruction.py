from ..instruction import Instruction
from abc import ABC, abstractmethod

class X86Instruction(Instruction, ABC):
	
	@abstractmethod
	def sets_zero_flag(self):
		pass
