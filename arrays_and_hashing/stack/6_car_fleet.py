from typing import List

# 853. Car Fleet
# Medium

# There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

# You are given two integer array position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

# A car fleet is a car or cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

# If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

# Return the number of car fleets that will arrive at the destination.


# Example 1:

# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

# Output: 3

# Explanation:

# The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
# The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
# The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
# Example 2:

# Input: target = 10, position = [3], speed = [3]

# Output: 1

# Explanation:

# There is only one car, hence there is only one fleet.
# Example 3:

# Input: target = 100, position = [0,2,4], speed = [4,2,1]

# Output: 1

# Explanation:

# The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The car starting at 4 (speed 1) travels to 5.
# Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.


# Constraints:

# n == position.length == speed.length
# 1 <= n <= 105
# 0 < target <= 106
# 0 <= position[i] < target
# All the values of position are unique.
# 0 < speed[i] <= 106


class Solution:
    # Time: O(nlogn)
    # Space: O(n)
    def car_fleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        # Combine positions and speeds into a list of tuples and sort them in descending order by position
        cars = sorted(zip(positions, speeds), reverse=True)

        # Initialize an empty stack to keep track of car fleets
        stack = []

        # Iterate through each car's position and speed
        for position, speed in cars:
            # Calculate the distance to the target
            distance = target - position
            # Calculate the time it takes for the car to reach the target
            time = distance / speed
            # If the stack is empty or the current car's time is greater than the time at the top of the stack,
            # it means this car cannot catch up to the fleet in front of it, so it forms a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)

        # The number of fleets is the size of the stack
        return len(stack)

    def main(self):
        target = 12
        position = [10, 8, 0, 5, 3]
        speed = [2, 4, 1, 1, 3]
        print(f"Input: target = {target}, position = {position}, speed = {speed}")
        print(f"Output: {self.car_fleet(target, position, speed)}")

        target = 10
        position = [3]
        speed = [3]
        print(f"Input: target = {target}, position = {position}, speed = {speed}")
        print(f"Output: {self.car_fleet(target, position, speed)}")

        target = 100
        position = [0, 2, 4]
        speed = [4, 2, 1]
        print(f"Input: target = {target}, position = {position}, speed = {speed}")
        print(f"Output: {self.car_fleet(target, position, speed)}")


if __name__ == "__main__":
    Solution().main()
