import timeit
from typing import List


class validAnagram:
    # Time: O(n)
    def hash_table(self, s: str, t: str) -> bool:
        from collections import Counter

        return Counter(s) == Counter(t)

    # Time: O(n)
    def array(self, s: str, t: str) -> bool:
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord("a")] += 1
        for char in t:
            counts[ord(char) - ord("a")] -= 1
            if counts[ord(char) - ord("a")] < 0:
                return False
        return all(count == 0 for count in counts)

    # Time: O(nlogn)
    def sorted_anagrams(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def main(self):
        s = "anagram"
        t = "nagaram"
        funcs = [self.hash_table, self.array, self.sorted_anagrams]
        for func in funcs:
            start_time = timeit.default_timer()
            print(func(s, t))
            end_time = timeit.default_timer()
            print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds.")


if __name__ == "__main__":
    validAnagram().main()
