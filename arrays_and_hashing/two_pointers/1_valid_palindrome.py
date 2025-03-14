# 125. Valid Palindrome
# Easy

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


# Constraints:

# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.


class Solution:
    # Time: O(n)
    # Space: O(1)
    def is_palindrome(self, s: str) -> bool:
        # Initialize two pointers at the start (left) and end (right) of the string
        left, right = 0, len(s) - 1

        # Continue until the two pointers meet
        while left < right:
            # If the character at the left pointer is not alphanumeric, move the pointer to the right
            while left < right and not s[left].isalnum():
                left += 1
            # If the character at the right pointer is not alphanumeric, move the pointer to the left
            while left < right and not s[right].isalnum():
                right -= 1

            # If the characters at the left and right pointers (converted to lowercase) are not the same, return False
            if s[left].lower() != s[right].lower():
                return False
            # Move the left pointer to the right and the right pointer to the left
            left += 1
            right -= 1

        # If all pairs of characters have been checked and are the same, return True
        return True

    def main(self):
        s = "A man, a plan, a canal: Panama"
        print(f"Input: s = {s}")
        print(f"Output: {self.is_palindrome(s)}")

        s = "race a car"
        print(f"Input: s = {s}")
        print(f"Output: {self.is_palindrome(s)}")

        s = " "
        print(f"Input: s = {s}")
        print(f"Output: {self.is_palindrome(s)}")


if __name__ == "__main__":
    Solution().main()
