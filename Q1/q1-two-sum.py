"""
 * q1-two-sum.py
 *
 * @param List nums
 * @param int target
 *
 * @return List indexes
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_map = {}

        for idx, val in enumerate(nums):
            num_map[val] = idx

        for idx, val in enumerate(nums):
            target_map_input = target - val
            if (target_map_input in num_map) and (num_map[target_map_input] > idx):
                return [idx+1, num_map[target_map_input]+1]

        return []

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
