import asm.x86.x86_instruction
import asm.x86.instructions

class Line(object):
	instruction = None
	arguments = []
	
class Assembly(object):
	lines = []