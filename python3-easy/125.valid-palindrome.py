#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
import re
class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        clean = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(clean)
        return clean == clean[::-1]
    

if __name__ == "__main__":
    s = Solution()
    s.isPalindrome("A man, a plan, a canal: Panama")
# @lc code=end

