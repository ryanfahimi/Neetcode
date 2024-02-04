import timeit
from typing import List


class groupAnagrams:
    # Time: O(nklogk)
    # Space: O(nk)
    def sorted_hash_table(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            # sorted() returns a list
            key = tuple(sorted(s))  # Convert the list to a tuple
            # If the key is not in the dictionary, then add it
            anagrams[key] = anagrams.get(key, []) + [s]
        return list(anagrams.values())

    # Time: O(nk)
    # Space: O(nk)
    def count_hash_table(self, strs: List[str]) -> List[List[str]]:
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
            # If the key is not in the dictionary, then add it
            anagrams[key] = anagrams.get(key, []) + [s]
        return list(anagrams.values())

    def main(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        funcs = [self.sorted_hash_table, self.count_hash_table]
        for func in funcs:
            start_time = timeit.default_timer()
            print(func(strs))
            end_time = timeit.default_timer()
            print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds.")


if __name__ == "__main__":
    groupAnagrams().main()
