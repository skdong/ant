class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        nums = [gas[i]-cost[i] for i in range(len(gas))]

        for i in range(len(gas)):

            if nums[i] < 0:
                continue

        return -1


gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
Solution().canCompleteCircuit(gas, cost)