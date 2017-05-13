package x86

type push struct {
	Instruction
}

func (i push) Max_arguments() int {
    return 1
}

func (i push) Sets_zero_flag() bool {
	return false
}
