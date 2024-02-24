"""here we use two pass approach to solve this problem. In the first pass we calculate the prefix product of the array and in the second pass we calculate the postfix product of the array. Then we multiply the prefix and postfix product to get the final result. This approach is O(n) time and O(1) space complexity.
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]

        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res