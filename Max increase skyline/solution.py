"""in this I just got the difference between the maximum of the row and column of that specific element and find the minimum of the two and subtract the element from it. 
"""
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        cnt=0
        column_list=[]
        for i in range(len(grid)):
            column_array = []
            for row in range(len(grid)):
                column_array.append(grid[row][i])
            column_list.append(column_array)
        for j in range(len(grid)):
            for i in range(len(grid)):
                cnt+=abs(min(max(grid[j]),max(column_list[i]))-grid[j][i])
        
        return cnt