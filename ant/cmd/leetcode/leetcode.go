package main

import (
	"github.com/skdong/ant/ant/pkg/leetcode"
	"fmt"
)

func try_make(m,n int){
	recoder := make([][]int, m)
	for i:=0; i<m; i++{
		recoder[i] = make([]int, n)
	}
	for _, line := range recoder{
		for _, skip := range line{
			fmt.Print(skip)
		}
		fmt.Println("")
	}
}
 
func main(){
	try_make(7,3)

	fmt.Println(leetcode.UniquePaths(7,3))
}