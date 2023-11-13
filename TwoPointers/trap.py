from typing import List


class trap:
    def two_pointers(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        total = 0
        while left < right:
            if height[left] < height[right]:
                left += 1
                max_left = max(max_left, height[left])
                # Add the difference between the max height and the current height
                total += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                # Add the difference between the max height and the current height
                total += max_right - height[right]
        return total

    def main(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        print(self.two_pointers(height))


if __name__ == "__main__":
    trap().main()
