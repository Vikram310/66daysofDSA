# Two pointer approach
class Solution(object):
    def sortedsquares(self, nums):
        result = [None for _ in nums]
        left, right = 0, len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
        return result

# one liner solution
class Solution(object):
    def sortedSquares(self, nums):
        return sorted ([i*i for i in nums])