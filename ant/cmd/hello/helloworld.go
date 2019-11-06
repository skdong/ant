package main

import (
	"fmt"
)

var num []int

func fab(n int) int{
	fmt.Println(n)
	if n == 0{
		return 0
	}else if n <= 2{
		return 1
	}else{
		return fab(n-1) + fab(n-2)
	}
}

func fab_num(n int) int{
	if num[n] == 0{
		fmt.Printf("num %v\n",n)
		if n == 0{
			num[n] = 0
		}else if n <= 2{
			num[n] = 1
		}else{
			num[n] = fab_num(n-1) + fab_num(n-2)
		}
	}
	return num[n]
}



func main(){
	num = make([]int , 100)
	fmt.Println(fab_num(10))
	
}