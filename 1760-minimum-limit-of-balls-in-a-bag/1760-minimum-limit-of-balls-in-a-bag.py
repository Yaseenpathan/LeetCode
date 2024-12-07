class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        def canDivide(maxPenalty):
            operations = 0
            for b in nums:
                operations += (b - 1) // maxPenalty
                if operations > maxOperations:
                    return False
            return True

        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if canDivide(mid):
                right = mid  
            else:
                left = mid + 1  
        return left