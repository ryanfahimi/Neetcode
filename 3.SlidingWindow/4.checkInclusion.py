# 567. Permutation in String
# Medium

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.


# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false


# Constraints:

# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.


class CheckInclusion:
    # Time: O(n)
    def array(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, return False as s1 cannot be a permutation of s2
        if len(s1) > len(s2):
            return False

        # Initialize frequency count arrays for s1 and the sliding window in s2
        s1Count, windowCount = [0] * 26, [0] * 26

        # Count the frequency of each character in s1 and the first 'len(s1)' characters in s2
        for right in range(len(s1)):
            s1Count[ord(s1[right]) - ord("a")] += 1
            windowCount[ord(s2[right]) - ord("a")] += 1

        # If the frequencies match, return True
        if windowCount == s1Count:
            return True

        # Initialize the left pointer of the sliding window
        left = 0

        # Slide the window over s2
        for right in range(len(s1), len(s2)):
            # Remove the character at the left of the window from the window count
            windowCount[ord(s2[left]) - ord("a")] -= 1
            # Add the character at the right of the window to the window count
            windowCount[ord(s2[right]) - ord("a")] += 1
            # If the frequencies match, return True
            if windowCount == s1Count:
                return True
            # Move the left pointer of the window to the right
            left += 1

        # If no match is found, return False
        return False

    # Time: O(n)
    def matches(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, return False as s1 cannot be a permutation of s2
        if len(s1) > len(s2):
            return False

        # Initialize frequency count arrays for s1 and the sliding window in s2
        s1Count, windowCount = [0] * 26, [0] * 26

        # Count the frequency of each character in s1 and the first 'len(s1)' characters in s2
        for right in range(len(s1)):
            s1Count[ord(s1[right]) - ord("a")] += 1
            windowCount[ord(s2[right]) - ord("a")] += 1

        # Initialize a counter for the number of characters with matching frequencies in s1 and the window
        matches = 0
        for ch in range(26):
            matches += s1Count[ch] == windowCount[ch]

        # Initialize the left pointer of the sliding window
        left = 0

        # Slide the window over s2
        for right in range(len(s1), len(s2)):
            # If all characters have matching frequencies, return True
            if matches == 26:
                return True

            # Add the character at the right of the window to the window count
            rightCharIndex = ord(s2[right]) - ord("a")
            windowCount[rightCharIndex] += 1
            # If the frequencies match, increment the matches counter
            if windowCount[rightCharIndex] == s1Count[rightCharIndex]:
                matches += 1
            # If the window count exceeds the s1 count, decrement the matches counter
            elif windowCount[rightCharIndex] == s1Count[rightCharIndex] + 1:
                matches -= 1

            # Remove the character at the left of the window from the window count
            leftCharIndex = ord(s2[left]) - ord("a")
            windowCount[leftCharIndex] -= 1
            # If the frequencies match, increment the matches counter
            if windowCount[leftCharIndex] == s1Count[leftCharIndex]:
                matches += 1
            # If the window count falls below the s1 count, decrement the matches counter
            elif windowCount[leftCharIndex] == s1Count[leftCharIndex] - 1:
                matches -= 1

            # Move the left pointer of the window to the right
            left += 1

        # If all characters have matching frequencies at the end of the sliding window, return True
        return matches == 26

    def main(self):
        s1 = "ab"
        s2 = "eidbaooo"
        print(f"Input: s1 = {s1}, s2 = {s2}")
        print(f"Array Output: {self.array(s1, s2)}")
        print(f"Matches Output: {self.matches(s1, s2)}")

        s1 = "ab"
        s2 = "eidboaoo"
        print(f"Input: s1 = {s1}, s2 = {s2}")
        print(f"Array Output: {self.array(s1, s2)}")
        print(f"Matches Output: {self.matches(s1, s2)}")


if __name__ == "__main__":
    CheckInclusion().main()
