package x86

type proc struct {
	Instruction
}

func (i proc) Max_arguments() int {
    return 1
}