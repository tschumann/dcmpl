package x86

type mov struct {
	Instruction
}

func (i mov) Max_arguments() int {
    return 5
}

func (i mov) Sets_zero_flag() bool {
	return false
}
