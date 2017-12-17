from .add import Add
from .align import Align
from .call import Call
from .cmp import Cmp
from .inc import Inc
from .jmp import Jmp
from .jnz import Jnz
from .jz import Jz
from .mov import Mov
from .pop import Pop
from .public import Public
from .push import Push
from .retn import Retn
from .test import Test

def get_instructions():
	return {
		"add": Add,
		"align": Align,
		"call": Call,
		"public": Public,
		"retn": Retn,
		"test": Test
	}
