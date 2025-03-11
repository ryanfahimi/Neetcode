from typing import List

# 4. Median of Two Sorted Arrays
# Hard

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).


# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


# Constraints:


# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106
class FindMedianSortedArrays:
    # Time: O(m+n)
    def by_recursive(self, nums1: List[int], nums2: List[int]) -> float:
        # Helper function to find the k-th element in the merged array
        def find_kth_element(nums1, nums2, k):
            # If one array is empty, the kth element is from the other array.
            if not nums1:
                return nums2[k - 1]
            if not nums2:
                return nums1[k - 1]
            # If k is 1, return the minimum of the first elements.
            if k == 1:
                return min(nums1[0], nums2[0])

            # Determine the indices to compare in each array.
            mid1 = min(len(nums1), k // 2)
            mid2 = min(len(nums2), k // 2)

            # Eliminate the first mid1 or mid2 elements from one of the arrays.
            if nums1[mid1 - 1] <= nums2[mid2 - 1]:
                # Exclude the first mid1 elements from nums1 and adjust k accordingly.
                return find_kth_element(nums1[mid1:], nums2, k - mid1)
            else:
                # Exclude the first mid2 elements from nums2 and adjust k accordingly.
                return find_kth_element(nums1, nums2[mid2:], k - mid2)

        total_length = len(nums1) + len(nums2)
        if total_length % 2 == 1:
            # Odd total length: the median is the middle element.
            return float(find_kth_element(nums1, nums2, total_length // 2 + 1))
        else:
            # Even total length: the median is the average of the two middle elements.
            return (
                find_kth_element(nums1, nums2, total_length // 2)
                + find_kth_element(nums1, nums2, total_length // 2 + 1)
            ) / 2.0

    # Time: O(log(min(m,n)))
    def by_optimal(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to minimize the binary search range
        if len(nums1) > len(nums2):
            return self.by_optimal(nums2, nums1)

        total_length = len(nums1) + len(nums2)
        half_length = total_length // 2

        left, right = 0, len(nums1) - 1

        while True:
            # Partition nums1 and nums2
            partition1 = (left + right) // 2
            partition2 = half_length - partition1 - 2

            # Find the elements around the partition
            max_left1 = nums1[partition1] if partition1 >= 0 else float("-inf")
            min_right1 = (
                nums1[partition1 + 1] if partition1 + 1 < len(nums1) else float("inf")
            )

            max_left2 = nums2[partition2] if partition2 >= 0 else float("-inf")
            min_right2 = (
                nums2[partition2 + 1] if partition2 + 1 < len(nums2) else float("inf")
            )

            # Check if we have found the correct partitions
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # If the total length is even, return the average of the two middle elements
                if total_length % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else:
                    # If the total length is odd, return the middle element
                    return float(min(min_right1, min_right2))
            elif max_left1 > min_right2:
                # Move the partition in nums1 to the left
                right = partition1 - 1
            else:
                # Move the partition in nums1 to the right
                left = partition1 + 1

    def main(self):
        nums1 = [1, 3]
        nums2 = [2]
        print(f"Input: nums1 = {nums1}, nums2 = {nums2}")
        print(f"Output (Recursive): {self.by_recursive(nums1, nums2)}")
        print(f"Output (Optimal): {self.by_optimal(nums1, nums2)}")

        nums1 = [1, 2]
        nums2 = [3, 4]
        print(f"Input: nums1 = {nums1}, nums2 = {nums2}")
        print(f"Output (Recursive): {self.by_recursive(nums1, nums2)}")
        print(f"Output (Optimal): {self.by_optimal(nums1, nums2)}")


if __name__ == "__main__":
    FindMedianSortedArrays().main()
