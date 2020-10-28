# 괄호가 문법에 맞게 올바르게 닫혔는 지 확인하는 문제
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# Example 3:

# Input: s = "(]"
# Output: false

# Example 4:

# Input: s = "([)]"
# Output: false

# Example 5:

# Input: s = "{[]}"
# Output: true


# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                item = stack.pop()
                if i == ")":
                    if item != "(":
                        return False
                if i == "}":
                    if item != "{":
                        return False
                if i == "]":
                    if item != "[":
                        return False
        if len(stack) > 0:
            return False
        return True
