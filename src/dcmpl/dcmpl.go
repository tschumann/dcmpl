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
	
	lines := strings.Split(string(data), "\n")
	
	output, err := os.Create(filename + ".c")

	if err != nil {
		fmt.Println("Error opening file: ", err)
		os.Exit(1)
	}

	registers := make(map[string]int)
	
	for i := 0; i < len(lines); i++ {
		tokens := strings.Fields(lines[i])
		
		if len(tokens) == 0 {
			continue
		}
		
		for j := 0; j < len(tokens); j++ {
			// ignore everything after a comment
			if tokens[j] == ";" {
				continue
			}

			fmt.Println(tokens[j])
			match, _ := regexp.MatchString("\\.\\w+:\\d+", tokens[j])

			// ignore IDA's line prefix that contains segment and address data
			if match == true {
				continue
			}
			
			if tokens[j] == "push" {
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
				output.Write([]byte(tokens[j + 1] + " = " + tokens[j + 2] + ";\n"));
			} else if tokens[j] == "inc" {
				output.Write([]byte(tokens[j + 1] + "++;\n"));
			}
			
			fmt.Println(tokens[j])
		}
	}
	
	fmt.Println(registers)
}