class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        counter_n = [0]*10
        n = N
        while n > 0:
            counter_n[n%10] += 1
            n /= 10
        for i in range(32):
            counter_2 = [0]*10
            n2 = 2**i
            if n2 > N*10:
                break
            while n2 > 0:
                counter_2[n2%10] += 1
                n2 = n2/10
            for i in range(10):
                if counter_n[i] != counter_2[i]:
                    break
            else:
                return True
        return False

print Solution().reorderedPowerOf2(10)