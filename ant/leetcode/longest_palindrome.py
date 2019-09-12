class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palinds = dict()
        for i in range(len(s)):
            if i + 1< len(s):
                if s[i] == s[i+1]:
                    palin_len = 2
                    while i - palin_len / 2 >= 0 and i + palin_len/2 < len(s) and s[i-palin_len/2] == s[i+palin_len/2]:
                        palin_len +=2
                    if palin_len not in palinds:
                        palinds[palin_len] = s[i-palin_len/2:i+palin_len/2]