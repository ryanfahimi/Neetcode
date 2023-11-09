import timeit
from collections import Counter


class validAnagram:
    # Time: O(nlogn)
    def sorted(self, s: str, t: str) -> bool:
        # sorted() returns a list
        return sorted(s) == sorted(t)

    # Time: O(n)
    def hash_table(self, s: str, t: str) -> bool:
        # Counter() returns a dictionary
        return Counter(s) == Counter(t)

    # Time: O(n)
    def array(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = [0] * 26  # 26 letters in the alphabet
        for char in s:
            # ord() returns the unicode code point of a character
            counts[ord(char) - ord("a")] += 1
        for char in t:
            counts[ord(char) - ord("a")] -= 1
            # If the count is negative, then there are more of that character in t
            if counts[ord(char) - ord("a")] < 0:
                return False
        # If all counts are 0, then s and t are anagrams
        return all(count == 0 for count in counts)

    def main(self):
        s = "anagram"
        t = "nagaram"
        funcs = [self.sorted, self.hash_table, self.array]
        for func in funcs:
            start_time = timeit.default_timer()
            print(func(s, t))
            end_time = timeit.default_timer()
            print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds.")


if __name__ == "__main__":
    validAnagram().main()
