package main

import "fmt"
import "io/ioutil"
import "os"
import "regexp"
import "strings"

func indent(output *os.File, level int) {
	for i := 0; i < level; i++ {
		output.Write([]byte("\t"))
	}
}

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

	// go through and strip out all comments and commas etc
	for i := 0; i < len(raw_lines); i++ {
		tokens := strings.Fields(raw_lines[i])
		line := ""
		
		if len(tokens) == 0 {
			continue
		}
		
		for j := 0; j < len(tokens); j++ {
			token := tokens[j]
			if token[len(token) - 1:] == "," {
				token = tokens[j][:len(tokens[j]) - 1]
			}

			match, _ := regexp.MatchString("\\.\\w+:\\d+", token)

			// ignore IDA's line prefix that contains segment and address data
			if match == true {
				continue
			}
			
			if token[0:1] == ";" {
				// skip comments
				break
			}
			
			line += token
			line += " "
		}
		
		if len(line) > 0 {
			lines = append(lines, line)
		}
	}
	
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
		
		// TODO: some things just won't be instructions e.g. labels so this isn't so good
		if instruction_data == nil {
			fmt.Println("No instruction data for", instruction);
		} else {
			line := asm.Line{}
			line.Instruction = instruction_data
			// TODO: add arguments here too, after checking below
			assembly.Lines.PushBack(line)
			
			// subtract one for the instruction itself
			if len(tokens) - 1 > instruction_data.Max_arguments() {
				fmt.Println("Instruction", instruction, "has", len(tokens), "arguments - expected at most", instruction_data.Max_arguments())
				fmt.Println(tokens)
				os.Exit(1)
			}
		}
		
		var previous_line []string
		var previous_instruction string

		if i > 0 {
			previous_line = strings.Fields(lines[i - 1])
			previous_instruction = previous_line[0]
		}
		
		for j := 0; j < len(tokens); j++ {
			if tokens[j] == "jmp" {
				indent(output, indentation)
				if tokens[j + 1] == "short" {
					output.Write([]byte("goto " + tokens[j + 2] + ";\n"))
				}
			} else if tokens[j] == "jz" && previous_line != nil {
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
}