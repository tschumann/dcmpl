package x86

type inc struct {
	Instruction
}

func (i inc) Max_arguments() int {
    return 1
}