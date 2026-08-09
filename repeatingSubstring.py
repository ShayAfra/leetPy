# 459. Repeated Substring Pattern
# Easy
# Topics
# premium lock iconCompanies

# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.

# Example 2:

# Input: s = "aba"
# Output: false

# Example 3:

# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

 

# Constraints:

#     1 <= s.length <= 104
#     s consists of lowercase English letters.


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sub = ""
        for char in s:
            sub += char
            repetitionCount = (len(s)//len(sub))
            if sub * repetitionCount == s and repetitionCount >= 2:
                    return True
        return False