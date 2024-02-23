"""
The solution uses a dictionary to store the range of consecutive numbers. In the first pass over the array, each number is added to the dictionary as a key with a tuple as its value. The tuple contains the same number twice, indicating that the longest sequence it belongs to, at this point, is just the number itself.

During the second pass, if a number in the array has adjacent numbers that were also in the array, the dictionary is updated. The number's tuple is updated to reflect the range of the longest sequence of consecutive numbers it belongs to. This is done by checking and updating the left and right boundaries of the sequence.

The leftmost and rightmost numbers of the sequence are easily found as they are stored as values in the dictionary for every number that is part of the sequence.
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        nums_map = {}
        longest_consecutive = 0
        for num in nums:
            if num not in nums_map:
                nums_map[num] = [num, num]
                left = num
                right = num

                # left neighbor - extend left range
                if num - 1 in nums_map:
                    left = nums_map[num - 1][0]

                # right neighbor - extend right range
                if num + 1 in nums_map:
                    right = nums_map[num + 1][1]
                nums_map[left] = [left, right]
                nums_map[right] = [left, right]
                longest_consecutive = max(longest_consecutive, right - left + 1)

        return longest_consecutive