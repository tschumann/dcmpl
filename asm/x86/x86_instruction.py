from ..instruction import Instruction
from abc import ABC, abstractmethod

class X86Instruction(Instruction, ABC):

	def is_floating_point_instruction(self):
		return self.uses_floating_point_stack()
	
	@abstractmethod
	def sets_zero_flag(self):
		pass

	def uses_floating_point_stack(self):
		False
