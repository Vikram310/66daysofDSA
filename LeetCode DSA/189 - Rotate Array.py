class Solution(object):
    def rotate(self, nums, k):
        def rev(nums,i,j):
            while(i<j):
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j -= 1
            return nums
        
        if k > len(nums):
            k %= len(nums)
        
        if k > 0:
            rev(nums,0, len(nums)-1) #reverse entire array
            rev(nums, 0, k-1) #reverse upto k elements
            rev(nums, k, len(nums)-1) #reverse other elements after k