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

        lastRepeating = -1
        longestSubstring = 0
        positions = {}
        for i in range(len(s)):
            if s[i] in positions and lastRepeating < positions[s[i]]:
                lastRepeating = positions[s[i]]
            if i-lastRepeating > longestSubstring:
                longestSubstring = i-lastRepeating
            positions[s[i]] = i
        print lastRepeating
        print longestSubstring
        print positions
        return longestSubstring

##------------------------------ Simple Testing Code ------------------------------##

solution = Solution()
longest_substring = solution.lengthOfLongestSubstring("abcabcbb")
print(longest_substring)
#longest_substring = solution.lengthOfLongestSubstring("bbbbb")
#print(longest_substring)
#longest_substring = solution.lengthOfLongestSubstring("aab")
#print(longest_substring)
