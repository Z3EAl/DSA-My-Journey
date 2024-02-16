"""
    This is the second type of the problems where we're looking for indices, so sorting is not necessary. What you'd want to do is to go over the array, and try to find two integers that sum up to a target value. Most of the times, in such a problem, using dictionary (hastable) helps. You try to keep track of you've observations in a dictionary and use it once you get to the results.

Note: try to be comfortable to use enumerate as it's sometime out of comfort zone for newbies. enumerate comes handy in a lot of problems (I mean if you want to have a cleaner code of course). If I had to choose three built in functions/methods that I wasn't comfortable with at the start and have found them super helpful, I'd probably say enumerate, zip and set.

Solution: In this problem, you initialize a dictionary (seen). This dictionary will keep track of numbers (as key) and indices (as value). So, you go over your array (line #1) using enumerate that gives you both index and value of elements in array. As an example, let's do nums = [2,3,1] and target = 3. Let's say you're at index i = 0 and value = 2, ok? you need to find value = 1 to finish the problem, meaning, target - 2 = 1. 1 here is the remaining. Since remaining + value = target, you're done once you found it, right? So when going through the array, you calculate the remaining and check to see whether remaining is in the seen dictionary (line #3). If it is, you're done! you're current number and the remaining from seen would give you the output (line #4). Otherwise, you add your current number to the dictionary (line #5) since it's going to be a remaining for (probably) a number you'll see in the future assuming that there is at least one instance of answer.
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, value in enumerate(nums): #1
            remaining = target - nums[i] #2
            if remaining in seen: #3
                return [i, seen[remaining]]  #4
            else:
                seen[value] = i  #5