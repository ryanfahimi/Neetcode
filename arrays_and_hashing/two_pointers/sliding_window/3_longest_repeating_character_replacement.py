# 424. Longest Repeating Character Replacement
# Medium

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.


# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.


# Constraints:

# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.
# 0 <= k <= s.length


class Solution:
    # Time: O(n)
    def character_replacement(self, s: str, k: int) -> int:
        # Create a hash map to store the frequency of each character
        chars_count = {}
        # Initialize the left pointer
        left = 0
        # Initialize the max count and max length
        max_count = max_length = 0
        # Iterate through the string
        for right in range(len(s)):
            # Add the character to the hash map and increment its frequency
            chars_count[s[right]] = chars_count.get(s[right], 0) + 1
            # Update the max count
            max_count = max(max_count, chars_count[s[right]])
            # Calculate the current length
            current_length = right - left + 1
            # If the current length minus the max count is greater than k
            if current_length - max_count > k:
                # Decrement the frequency of the character at the left pointer
                chars_count[s[left]] -= 1
                # Increment the left pointer
                left += 1
            # Update the max length
            max_length = max(max_length, right - left + 1)
        return max_length

    def main(self):
        s = "ABAB"
        k = 2
        print(f"Input: s = {s}, k = {k}")
        print(f"Output: {self.character_replacement(s, k)}")

        s = "AABABBA"
        k = 1
        print(f"Input: s = {s}, k = {k}")
        print(f"Output: {self.character_replacement(s, k)}")


if __name__ == "__main__":
    Solution().main()
