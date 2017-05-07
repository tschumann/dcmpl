package asm

import "container/list"

type Instruction interface {
}

type Line struct {
	Instruction Instruction
	Arguments []string
}

type Assembly struct {
	Lines list.List
}
