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
	
	lines := strings.Split(string(data), "\n")
	
	output, err := os.Create(filename + ".c")

	if err != nil {
		fmt.Println("Error opening file: ", err)
		os.Exit(1)
	}

	indentation := 0
	registers := make(map[string]int)
	
	for i := 0; i < len(lines); i++ {
		tokens := strings.Fields(lines[i])
		
		if len(tokens) == 0 {
			continue
		}
		
		for j := 0; j < len(tokens); j++ {
			match, _ := regexp.MatchString("\\.\\w+:\\d+", tokens[j])

			// ignore IDA's line prefix that contains segment and address data
			if match == true {
				continue
			}

			// TODO: can't change an array element?
			if tokens[j][len(tokens[j]) - 1:] == "," {
				var cropped = tokens[j][:len(tokens[j]) - 1]
				tokens[j] = cropped
			}

			if tokens[j][0:1] == ";" {
				// skip comments
				break
			} else if tokens[j] == "push" {
				register := tokens[j + 1]
				if _, ok := registers[register]; ok {
					registers[register]++
				} else {
					registers[register] = 1
				}
				
				// saving the value of a special register, so don't say anything
				if register == "esp" && registers[register] >= 2 {
					continue
				}
			} else if tokens[j] == "pop" {
				register := tokens[j + 1]
				registers[register]--
			} else if tokens[j] == "mov" {
				indent(output, indentation)
				if tokens[j + 2] == "offset" {
					output.Write([]byte(tokens[j + 1] + " = &" + tokens[j + 3] + ";\n"))
				} else {
					output.Write([]byte(tokens[j + 1] + " = " + tokens[j + 2] + ";\n"))
				}
			} else if tokens[j] == "inc" {
				indent(output, indentation)
				output.Write([]byte(tokens[j + 1] + "++;\n"))
			} else if tokens[j] == "call" {
				indent(output, indentation)
				output.Write([]byte(tokens[j + 1] + "();\n"))
			} else if tokens[j] == "retn" {
				indent(output, indentation)
				output.Write([]byte("return;\n"))
			} else if tokens[j] == "jmp" {
				indent(output, indentation)
				if tokens[j + 1] == "short" {
					output.Write([]byte("goto " + tokens[j + 2] + ";\n"))
				}
			} else {
				if len(tokens) > j + 1 {
					if tokens[j + 1] == "proc" {
						indent(output, indentation)
						output.Write([]byte("void *" + tokens[j] + "()\n"))
						output.Write([]byte("{\n"))
						indentation++
						break
					} else if tokens[j][len(tokens[j]) - 1:] == ":" {
						output.Write([]byte(tokens[j] + "\n"))
						break
					}
				}
			}			
			
			// fmt.Println(tokens[j])
		}
	}
	
	// fmt.Println(registers)
}