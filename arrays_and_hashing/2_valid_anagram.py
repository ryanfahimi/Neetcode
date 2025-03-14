from collections import Counter

# 242. Valid Anagram
# Easy

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false


# Constraints:

# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


class IsAnagram:
    # Time: O(n + m)
    # Space: O(1)
    def by_array_counting(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26  # 26 letters in the alphabet
        for char in s:
            # ord() returns the unicode code point of a character
            count[ord(char) - ord("a")] += 1
        for char in t:
            count[ord(char) - ord("a")] -= 1
            # If the count is negative, then there are more of that character in t
            if count[ord(char) - ord("a")] < 0:
                return False
        # If all counts are 0, then s and t are anagrams
        return all(count == 0 for count in count)

    # Time: O(nlogn + mlogm)
    # Space: O(1)
    def by_sorting(self, s: str, t: str) -> bool:
        # sorted() returns a list
        return sorted(s) == sorted(t)

    # Time: O(n + m)
    # Space: O(1)
    def by_hash_map_counting(self, s: str, t: str) -> bool:
        # Counter() returns a hash map
        return Counter(s) == Counter(t)

    def main(self):
        s, t = "anagram", "nagaram"
        print(f"Input: s = {s}, t = {t}")
        print(f"Array Counting Output: {self.by_array_counting(s, t)}")
        print(f"Sorting Output: {self.by_sorting(s, t)}")
        print(f"Hash Map Counting Output: {self.by_hash_map_counting(s, t)}")

        s, t = "rat", "car"
        print(f"Input: s = {s}, t = {t}")
        print(f"Array Counting Output: {self.by_array_counting(s, t)}")
        print(f"Sorting and Counting Output: {self.by_sorting(s, t)}")
        print(f"Hash Map Counting Output: {self.by_hash_map_counting(s, t)}")


if __name__ == "__main__":
    IsAnagram().main()
