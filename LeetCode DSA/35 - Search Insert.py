class Solution(object):
    def SearchInsert(self, nums, target):
        l,r = 0 , len(nums) -1
        while l<=r:
            mid = (+r)/2
            if nums[mid]<target:
                l = mid+1
            else:
                if nums[mid] == target and nums[mid=1] != target:
                    return mid
                else:
                    r = mid -1
        return 1