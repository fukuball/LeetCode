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

        longest_substring_length = [0]

        for i in range(len(s)):
            sub = s[i:]
            if len(sub) <= max(longest_substring_length):
                break
            longest_substring = []
            for c in sub:
                if c in longest_substring:
                    break
                else:
                    longest_substring.append(c)
            longest_substring_length.append(len(longest_substring))

        return max(longest_substring_length)

##------------------------------ Simple Testing Code ------------------------------##

solution = Solution()
longest_substring = solution.lengthOfLongestSubstring("abcabcbb")
print(longest_substring)
longest_substring = solution.lengthOfLongestSubstring("bbbbb")
print(longest_substring)
longest_substring = solution.lengthOfLongestSubstring("aab")
print(longest_substring)
