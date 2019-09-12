class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num_len = len(nums1) + len(nums2)
        nums1_cur = 0
        nums2_cur = 0
        mid = num_len / 2
        nums = list()
        for i in range(mid+1):
            if len(nums1) == nums1_cur:
                nums.extend(nums2[nums2_cur:])
                break
            elif len(nums2) == nums2_cur:
                nums.extend(nums1[nums1_cur:])
                break
            elif nums1[nums1_cur] > nums2[nums2_cur]:
                nums.append(nums2[nums2_cur])
                nums2_cur += 1
            else:
                nums.append(nums1[nums1_cur])
                nums1_cur += 1
        if num_len % 2 == 1:
            return nums.pop()
        else:
            return (nums.pop() + nums.pop())/2.0