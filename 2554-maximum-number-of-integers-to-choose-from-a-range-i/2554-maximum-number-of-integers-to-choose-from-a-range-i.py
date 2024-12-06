class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        banned_set = set(banned)
        choosen_count = 0
        current_sum = 0
        for num in range(1,n+1):
            if num in banned_set:
                continue
            
            if current_sum + num > maxSum:
                break
            
            current_sum += num
            choosen_count += 1
        
        return choosen_count
            