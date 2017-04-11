package x86

type jnz struct {
	Instruction
}

func (i jnz) Max_arguments() int {
    return 3
}

func (i jnz) Sets_zero_flag() bool {
	return false
}
