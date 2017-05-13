package x86

func Instruction_info() map[string]Instruction {
	instructions := map[string]Instruction {
		"call": call{},
		"cmp": cmp{},
		"inc": inc{},
		"jmp": jmp{},
		"jnz": jnz{},
		"jz": jz{},
		"mov": mov{},
		"pop": pop{},
		"push": push{},
		"retn": retn{},
		"test": test{},
	}

	return instructions
}
