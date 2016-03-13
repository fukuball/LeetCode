"""
 * median-of-two-sorted-arrays
 *
 * @param {array} nums1
 * @param {array} nums2
 *
 * @return {float}
"""


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        len_1 = len(nums1)
        len_2 = len(nums2)
        if (len_1 + len_2) % 2 == 1:
            return self.getKth(nums1, nums2, (len_1 + len_2)/2 + 1)
        else:
            return (self.getKth(nums1, nums2, (len_1 + len_2)/2) + self.getKth(nums1, nums2, (len_1 + len_2)/2 + 1)) * 0.5

    def getKth(self, nums1, nums2, k):
        len_1 = len(nums1)
        len_2 = len(nums2)
        if len_1 > len_2:
            return self.getKth(nums2, nums1, k)
        if len_1 == 0:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        middle_position = min(k/2, len_1)
        if nums1[middle_position-1] <= nums2[middle_position-1]:
            return self.getKth(nums1[middle_position:], nums2, k-middle_position)
        else:
            return self.getKth(nums1, nums2[middle_position:], k-middle_position)


##------------------------------ Simple Testing Code ------------------------------##

solution = Solution()
nums1 = [1, 3, 5, 7]
nums2 = [2, 4, 6, 8, 9, 10]
print(solution.findMedianSortedArrays(nums1, nums2))
nums1 = [2, 4, 6, 8, 9, 10]
nums2 = [1, 3, 5, 7]
print(solution.findMedianSortedArrays(nums1, nums2))
