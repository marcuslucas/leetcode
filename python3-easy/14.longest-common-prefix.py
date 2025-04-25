#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        if not strs or "" in strs:
            return ""
        for i in range(len(strs)):
                for j in range(min(len(res), len(strs[i]))):
                    if strs[i][j] != res[j]:
                        res = res[:j]
                        break
                    if res == "":
                        return ""
                    res = res[:len(strs[i])]
        return res
    
if __name__ == "__main__":
	s = Solution()
	s.longestCommonPrefix(["flower","flow","flight"])
# @lc code=end

