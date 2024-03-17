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
    def hashTable(self, s: str) -> int:
        # Create a dictionary to store the characters and their indices
        charDict = {}
        # Initialize the start of the window and the maximum length
        left, maxLength = 0, 0
        for right in range(len(s)):
            # If the character is in the dictionary
            if s[right] in charDict:
                # Update the start of the window
                left = max(left, charDict[s[right]] + 1)
            # Add the character and its index to the dictionary
            charDict[s[right]] = right
            # Update the maximum length
            maxLength = max(maxLength, right - left + 1)
        return maxLength

    # Time: O(n)
    def hashSet(self, s: str) -> int:
        # Create a set to store the characters
        charSet = set()
        # Initialize the start of the window and the maximum length
        left, maxLength = 0, 0
        for right in range(len(s)):
            # If the character is in the set
            while s[right] in charSet:
                # Remove the character at the start of the window
                charSet.remove(s[left])
                # Update the start of the window
                left += 1
            # Add the character to the set
            charSet.add(s[right])
            # Update the maximum length
            maxLength = max(maxLength, right - left + 1)
        return maxLength

    def main(self):
        s = "abcabcbb"
        print(f"Input: s = {s}")
        print(f"Hash Table Output: {self.hashTable(s)}")
        print(f"Hash Set Output: {self.hashSet(s)}")

        s = "bbbbb"
        print(f"Input: s = {s}")
        print(f"Hash Table Output: {self.hashTable(s)}")
        print(f"Hash Set Output: {self.hashSet(s)}")

        s = "pwwkew"
        print(f"Input: s = {s}")
        print(f"Hash Table Output: {self.hashTable(s)}")
        print(f"Hash Set Output: {self.hashSet(s)}")


if __name__ == "__main__":
    LengthOfLongestSubstring().main()
