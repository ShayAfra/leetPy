# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charS = {}
        charT = {}
        for char in s:
            if char not in charS:
                charS[char] = 1
            charS[char] += 1
        for char in t:
            if char not in charT:
                charT[char] = 1
            charT[char]+= 1
        if charS == charT:
            return True
        else:
            return False
        