# Given a string s, find the length of the longest substring without repeating characters.
# 중복되는 문자가 없는 가장 긴 문자열의 길이 구하기


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:

# Input: s = ""
# Output: 0


# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        queue = []
        for i in s:
            if i in queue:
                for _ in range(queue.index(i) + 1):
                    queue.pop(0)

                queue.append(i)
                if count < len(queue):
                    count = len(queue)
            else:
                queue.append(i)
                if count < len(queue):
                    count = len(queue)
        return count
