package x86

type jz struct {
	Instruction
}

func (i jz) Max_arguments() int {
    return 3
}

func (i jz) Sets_zero_flag() bool {
	return false
}
