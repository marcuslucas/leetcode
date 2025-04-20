#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prevMap = {}
        for i, n in enumerate(nums):
            if n in prevMap:
                return True
            prevMap[n] = i
        return False
# @lc code=end