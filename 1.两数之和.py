#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums=len(nums)
        for i in range(0,len_nums):
            for j in range(i+1,len_nums):
                if nums[i]+nums[j]==target:
                    return [i,j]

if __name__=="__main__":
    s=Solution()
    print(s.twoSum([3,4,6,11], 17))
# @lc code=end
