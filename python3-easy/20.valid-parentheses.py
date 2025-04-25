#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        closeOpen = {')':'(',']':'[','}':'{'}
        stack = []
        for char in s:
            if char in closeOpen:
                if stack and stack[-1] == closeOpen[char]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(char)
        return True if not stack else False
# @lc code=end

