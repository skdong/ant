package leetcode

var recoder [][]int
func uniquePaths(m, n int)int{
	if recoder == nil{
		recoder = make([][]int, m)
		for i:=0; i<m ; i++{
			recoder[i] = make([]int, n)
		}
	}
	if recoder[m-1][n-1] != 0 {
		return recoder[m-1][n-1]
	}

	if m == 1 && n == 1{
		recoder[m-1][n-1] = 1
	}else if m == 1{
		recoder[m-1][n-1] = uniquePaths(m, n-1)
	}else if n == 1{
		recoder[m-1][n-1] = uniquePaths(m-1, n)
	}else{
		recoder[m-1][n-1] = uniquePaths(m-1, n) + uniquePaths(m, n-1)
	}
	return recoder[m-1][n-1]
}

func UniquePaths(m, n int)int{
	return uniquePaths(m,n)
}