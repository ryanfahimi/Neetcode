from typing import List


class twoSum:
    # Time: O(n)
    # Space: O(n)
    def two_pointers(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left, right]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
        return []

    def main(self):
        numbers = [2, 7, 11, 15]
        target = 9
        print(self.two_pointers(numbers, target))


if __name__ == "__main__":
    twoSum().main()
