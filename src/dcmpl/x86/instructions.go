package x86

func Instruction_info() map[string]Instruction {
	instructions := map[string]Instruction {
		"call": call{},
		"inc": inc{},
		"jmp": jmp{},
		"mov": mov{},
		"pop": pop{},
		"push": push{},
		"retn": retn{},
	}

	return instructions
}