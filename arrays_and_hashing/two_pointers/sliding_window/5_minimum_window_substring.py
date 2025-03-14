# 76. Minimum Window Substring
# Hard

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.


# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.


# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.


# Follow up: Could you find an algorithm that runs in O(m + n) time?


class MinWindow:
    # Time: O(n^2)
    # Space: O(m)
    def by_brute_force(self, s: str, t: str) -> str:
        # Create a hash map to store the frequency of each character
        t_count, window_count = {}, {}
        # Iterate through the characters in t
        for ch in t:
            # Add the count of the character to t count
            t_count[ch] = t_count.get(ch, 0) + 1

        left = 0
        min_length = float("inf")
        result = ""

        # Iterate through the indeces of the characters in s
        for right in range(len(s)):
            # Add the count of the character to window count
            window_count[s[right]] = window_count.get(s[right], 0) + 1
            # While the window contains all the characters in t
            while left <= right and all(
                window_count.get(char, 0) >= count for char, count in t_count.items()
            ):
                # Update the result if the current window is smaller than the minimum window
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = s[left : right + 1]
                # Remove the count of the character from window count
                window_count[s[left]] -= 1
                left += 1

        return result

    # Time: O(n)
    # Space: O(m)
    def by_have_and_need(self, s: str, t: str) -> str:
        # Create a hash map to store the frequency of each character
        t_count, window_count = {}, {}
        # Iterate through the characters in t
        for ch in t:
            # Add the count of the character to t count
            t_count[ch] = t_count.get(ch, 0) + 1

        # Initialize the number of characters in t that are in the window
        have = 0
        # Initialize the number of characters in t that are needed in the window
        need = len(t_count)

        left = 0
        min_length = float("inf")
        result = ""
        # Iterate through the indeces of the characters in s
        for right in range(len(s)):
            # Add the count of the character to window count
            window_count[s[right]] = window_count.get(s[right], 0) + 1
            # If the character is in t and the count of the character in the window is equal to the count of the character in t
            if s[right] in t_count and window_count[s[right]] == t_count[s[right]]:
                # Increment the number of characters in t that are in the window
                have += 1

            # While the window contains all the characters in t
            while left <= right and have == need:
                # Update the result if the current window is smaller than the minimum window
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = s[left : right + 1]

                # Remove the count of the character from window count
                window_count[s[left]] -= 1
                # If the character is in t and the count of the character in the window is less than the count of the character in t
                if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                    # Decrement the number of characters in t that are in the window
                    have -= 1
                left += 1

        return result

    def main(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        print(f"Input: s = {s}, t = {t}")
        print(f"Brute Force Output: {self.by_brute_force(s, t)}")
        print(f"Hash Table Output: {self.by_have_and_need(s, t)}")

        s = "a"
        t = "a"
        print(f"Input: s = {s}, t = {t}")
        print(f"Brute Force Output: {self.by_brute_force(s, t)}")
        print(f"Have and Need Output: {self.by_have_and_need(s, t)}")

        s = "a"
        t = "aa"
        print(f"Input: s = {s}, t = {t}")
        print(f"Brute Force Output: {self.by_brute_force(s, t)}")
        print(f"Have and Need Output: {self.by_have_and_need(s, t)}")


if __name__ == "__main__":
    MinWindow().main()
