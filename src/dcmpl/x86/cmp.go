package x86

type cmp struct {
	Instruction
}

func (i cmp) Max_arguments() int {
    return 5
}

func (i cmp) Sets_zero_flag() bool {
	return true
}
