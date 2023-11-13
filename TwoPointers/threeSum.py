from typing import List


class threeSum:
    # Time: O(n^2)
    # Space: O(n)
    def two_pointers(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            # If the current number is the same as the previous number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum < 0:
                    left += 1
                elif curr_sum > 0:
                    right -= 1
                else:  # target == 0
                    result.append([nums[i], nums[left], nums[right]])
                    # If the next number is the same as the current number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # If the previous number is the same as the current number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # Move the pointers
                    left += 1
                    right -= 1
        return result
