package x86

type pop struct {
	Instruction
}

func (i pop) Max_arguments() int {
    return 1
}