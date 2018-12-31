package main

import "fmt"
import "io/ioutil"
import "os"
import "regexp"
import "strings"

func main() {
	if len(os.Args) != 2 {
		fmt.Println("No file specified")
		os.Exit(1)
	}

	filename := os.Args[1]
		
	data, err := ioutil.ReadFile(filename)

	if err != nil {
		fmt.Println("Error reading file: ", err)
		os.Exit(1)
	}
	
	raw_lines := strings.Split(string(data), "\n")
	lines := make([]string, 0)
	
	assembly := asm.Assembly{}
	// assembly.Lines := list.New()
	
	output, err := os.Create(filename + ".c")

	if err != nil {
		fmt.Println("Error opening file: ", err)
		os.Exit(1)
	}

	instructions := x86.Instruction_info()
	indentation := 0
	registers := make(map[string]int)
	
	for i := 0; i < len(lines); i++ {
		tokens := strings.Fields(lines[i])
		
		instruction := tokens[0]
		instruction_data := instructions[instruction]
		
		for j := 0; j < len(tokens); j++ {
			if tokens[j] == "jz" && previous_line != nil {
				var location string
				if tokens[j + 1] == "short" {
					location = tokens[j + 2]
				} else {
					location = tokens[j + 1]
				}

				if previous_instruction == "test" && previous_line[1] == previous_line[2] {
					indent(output, indentation)
					output.Write([]byte("if( " + previous_line[1] + " == 0 )\n"))
					indent(output, indentation)
					output.Write([]byte("{\n"))
					indentation++
					indent(output, indentation)
					output.Write([]byte("goto " + location + ";\n"))
					indentation--
					indent(output, indentation)
					output.Write([]byte("}\n"))
				} else if previous_instruction == "cmp" {
					indent(output, indentation)
					if previous_line[1] == "dword" && previous_line[2] == "ptr" {
						output.Write([]byte("if( " + previous_line[3] + " == " + previous_line[4] + " )\n"))
					} else {
						output.Write([]byte("if( " + previous_line[1] + " == " + previous_line[2] + " )\n"))
					}
					indent(output, indentation)
					output.Write([]byte("{\n"))
					indentation++
					indent(output, indentation)
					output.Write([]byte("goto " + location + ";\n"))
					indentation--
					indent(output, indentation)
					output.Write([]byte("}\n"))
				}
				break
			}		
		}
	}
}