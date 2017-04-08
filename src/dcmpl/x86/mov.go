package x86

type mov struct {
	Instruction
}

func (i mov) Max_arguments() int {
    return 5
}