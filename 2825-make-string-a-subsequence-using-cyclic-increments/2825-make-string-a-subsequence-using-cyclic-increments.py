class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        i, j = 0, 0
        n, m = len(str1), len(str2)

        while i < n and j < m:
            diff = (ord(str2[j]) - ord(str1[i])) % 26
            if diff == 0: 
                j += 1  
            elif diff == 1:  
                j += 1 
            i += 1

        return j == m  