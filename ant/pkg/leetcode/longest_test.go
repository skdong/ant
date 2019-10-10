package leetcode

import (
	"testing"
	"fmt"
	
)

func Test_longestPalindrome(t *testing.T){
	s := "aba"
	ret := longestPalindrome(s)
	fmt.Println(ret)
}