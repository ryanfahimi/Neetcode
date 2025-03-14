from typing import List

# 49. Group Anagrams
# Medium

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:

# Input: strs = [""]
# Output: [[""]]

# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


# Constraints:

# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.


class GroupAnagrams:
    # Time: O(nklogk)
    # Space: O(nk)
    def by_sorting(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            # sorted() returns a list
            key = tuple(sorted(s))  # Convert the list to a tuple
            # If the key is not in the hash map, then add it
            anagrams[key] = anagrams.get(key, []) + [s]
        return list(anagrams.values())

    # Time: O(nk)
    # Space: O(n)
    def by_counting(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            # Create a list of 26 zeros
            count = [0] * 26  # 26 letters in the alphabet
            for char in s:
                # ord() returns the unicode code point of a character
                # Subtracting the unicode code point of "a" from the unicode code point of the character
                # gives us the index of the character in the list
                count[ord(char) - ord("a")] += 1  # Increment the count of the character
            key = tuple(count)  # Convert the list to a tuple
            # If the key is not in the hash map, then add it
            anagrams[key] = anagrams.get(key, []) + [s]
        return list(anagrams.values())

    def main(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        print(f"Input: strs = {strs}")
        print(f"Sorting Output: {self.by_sorting(strs)}")
        print(f"Counting Output: {self.by_counting(strs)}")

        strs = [""]
        print(f"Input: strs = {strs}")
        print(f"Sorting Output: {self.by_sorting(strs)}")
        print(f"Counting Output: {self.by_counting(strs)}")

        strs = ["a"]
        print(f"Input: strs = {strs}")
        print(f"Sorting Output: {self.by_sorting(strs)}")
        print(f"Counting Output: {self.by_counting(strs)}")


if __name__ == "__main__":
    GroupAnagrams().main()
