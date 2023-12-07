package main

import ( "fmt"
		"os"
		"strings"
)


func check(e error) {
    if e != nil {
        panic(e)
    }
}

func main() {
    fmt.Println("Hello, World!")
	dat, err := os.ReadFile("test_input.txt")
	check(err)
	fmt.Printf("t1: %T\n", dat)

	res1 := strings.Split(string(dat), "\n")

	for _, element := range res1 {
		// index is the index where we are
		// element is the element from someSlice for where we are
		fmt.Println(element)
		fmt.Println("----------")
	}

}