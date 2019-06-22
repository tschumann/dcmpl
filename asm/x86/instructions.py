from .add import Add
from .align import Align
from .call import Call
from .cmp import Cmp
from .fcos import Fcos
from .fld import Fld
from .fldz import Fldz
from .fstp import Fstp
from .fsub import Fsub
from .inc import Inc
from .jmp import Jmp
from .jnz import Jnz
from .jz import Jz
from .label import Label
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
		"fcos": Fcos,
		"fld": Fld,
		"fldz": Fldz,
		"fstp": Fstp,
		"fsub": Fsub,
		"jmp": Jmp,
		"label": Label,
		"mov": Mov,
		"public": Public,
		"retn": Retn,
		"test": Test
	}
