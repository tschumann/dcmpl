from .call import Call
from .cmp import Cmp
from .inc import Inc
from .jmp import Jmp
from .jnz import Jnz
from .jz import Jz
from .mov import Mov
from .pop import Pop
from .proc import Proc
from .push import Push
from .retn import Retn
from .test import Test

def get_instructions():
	return {
		"retn": Retn,
		"test": Test
	}