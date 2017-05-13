package x86

type retn struct {
	Instruction
}

func (i retn) Max_arguments() int {
    return 0
}

func (i retn) Sets_zero_flag() bool {
	return false
}
