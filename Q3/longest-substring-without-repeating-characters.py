"""
 * longest-substring-without-repeating-characters.py
 *
 * @param {string} s
 *
 * @return {int}
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        last_repeating = -1
        longest_substring = 0
        positions = {}
        for i in range(len(s)):
            if s[i] in positions and last_repeating < positions[s[i]]:
                last_repeating = positions[s[i]]
            if i-last_repeating > longest_substring:
                longest_substring = i-last_repeating
            positions[s[i]] = i
        return longest_substring

##------------------------------ Simple Testing Code ------------------------------##

solution = Solution()
longest_substring = solution.lengthOfLongestSubstring("abcabcdb")
print(longest_substring)
longest_substring = solution.lengthOfLongestSubstring("bbbbb")
print(longest_substring)
longest_substring = solution.lengthOfLongestSubstring("aab")
print(longest_substring)
