package x86

type test struct {
	Instruction
}

func (i test) Max_arguments() int {
    return 2
}

func (i test) Sets_zero_flag() bool {
	return true
}
