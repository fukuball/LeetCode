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

        longest_substring = []

        for c in s:
            if c in longest_substring:
                return len(longest_substring)
            else:
                longest_substring.append(c)

        return len(longest_substring)

##------------------------------ Simple Testing Code ------------------------------##

solution = Solution()
longest_substring = solution.lengthOfLongestSubstring("abcabcbb")
print(longest_substring)
longest_substring = solution.lengthOfLongestSubstring("bbbbb")
print(longest_substring)
longest_substring = solution.lengthOfLongestSubstring("aab")
print(longest_substring)
