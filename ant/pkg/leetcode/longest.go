package leetcode

import (
	"strconv"
)

func longestPalindrome(s string) string {
	var check_palindrome func(s string)bool
	check_palindrome = func(palindrome string)bool{
		leng := len(palindrome)
		for i:=0; i<leng/2 ; i++{
			if palindrome[i] != palindrome[leng-i-1]{
				return false
			}
		}
		return true
	}
	
	ret := check_palindrome(s)
	return strconv.FormatBool(ret)
}