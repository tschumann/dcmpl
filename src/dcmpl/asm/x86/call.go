package x86

type call struct {
	Instruction
}

func (i call) Max_arguments() int {
    return 1
}

func (i call) Sets_zero_flag() bool {
	return false
}
