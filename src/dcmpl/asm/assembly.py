import asm.x86.x86_instruction
import asm.x86.instructions

# TODO: this should be a generic getter based on whatever CPU is currently being looked at
def get_x86_instructions():
	return asm.x86.instructions.get_instructions()

class Line(object):
	instruction = None
	arguments = []
	
class Assembly(object):
	lines = []