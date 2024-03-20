# 3. Longest Substring Without Repeating Characters
# Medium

# Given a string s, find the length of the longest substring without repeating characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Constraints:

# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.


class LengthOfLongestSubstring:
    # Time: O(n)
    def by_hash_map(self, s: str) -> int:
        # Create a hash map to store the characters and their indices
        characters = {}
        # Initialize the start of the window and the maximum length
        left, max_length = 0, 0
        for right in range(len(s)):
            # If the character is in the hash map
            if s[right] in characters:
                # Update the start of the window
                left = max(left, characters[s[right]] + 1)
            # Add the character and its index to the hash map
            characters[s[right]] = right
            # Update the maximum length
            max_length = max(max_length, right - left + 1)
        return max_length

    # Time: O(n)
    def by_hash_set(self, s: str) -> int:
        # Create a set to store the characters
        char_set = set()
        # Initialize the start of the window and the maximum length
        left, max_length = 0, 0
        for right in range(len(s)):
            # If the character is in the set
            while s[right] in char_set:
                # Remove the character at the start of the window
                char_set.remove(s[left])
                # Update the start of the window
                left += 1
            # Add the character to the set
            char_set.add(s[right])
            # Update the maximum length
            max_length = max(max_length, right - left + 1)
        return max_length

    def main(self):
        s = "abcabcbb"
        print(f"Input: s = {s}")
        print(f"Hash Map Output: {self.by_hash_map(s)}")
        print(f"Hash Set Output: {self.by_hash_set(s)}")

        s = "bbbbb"
        print(f"Input: s = {s}")
        print(f"Hash Map Output: {self.by_hash_map(s)}")
        print(f"Hash Set Output: {self.by_hash_set(s)}")

        s = "pwwkew"
        print(f"Input: s = {s}")
        print(f"Hash Map Output: {self.by_hash_map(s)}")
        print(f"Hash Set Output: {self.by_hash_set(s)}")


if __name__ == "__main__":
    LengthOfLongestSubstring().main()
