package leetcode

func maxSubArray(nums []int) int{
	n := len(nums)
	max := nums[0]
	accum := 0
	for i := 0; i < n ; i++{
		if accum < 0{
			accum = nums[i]
		}else{
			accum += nums[i]
		}
		if accum > max{
			max = accum
		}
	}
	return max
}