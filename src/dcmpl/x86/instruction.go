package x86

import "../asm"

type Instruction interface {
	asm.Instruction
	Max_arguments() int
	Sets_zero_flag() bool
}