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
from .or_ import Or
from .pop import Pop
from .push import Push
from .retn import Retn
from .test import Test
from ..public import Public
from ..var import Var

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
		"or": Or,
		"public": Public,
		"retn": Retn,
		"test": Test,
		"var": Var
	}
