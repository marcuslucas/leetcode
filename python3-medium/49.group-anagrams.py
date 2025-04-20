#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            hashMap[tuple(count)].append(word)
        return list(hashMap.values())

if __name__ == "__main__":
    s = Solution()
    s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
# @lc code=end

