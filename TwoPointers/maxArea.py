from typing import List


class maxArea:
    # Time: O(n)
    # Space: O(1)
    def two_pointers(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            # Calculate the area
            area = min(height[left], height[right]) * (right - left)
            # Update the max area
            max_area = max(max_area, area)
            # Move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

    def main(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        print(self.two_pointers(height))


if __name__ == "__main__":
    maxArea().main()
