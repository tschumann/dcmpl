package x86

type jmp struct {
	Instruction
}

func (i jmp) Max_arguments() int {
    return 2
}