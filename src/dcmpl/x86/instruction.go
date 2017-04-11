package x86

type Instruction interface {
	Max_arguments() int
	Sets_zero_flag() bool
}