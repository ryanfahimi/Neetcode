import timeit


class checkInclusion:
    # Time: O(n)
    # Space: O(1)
    def array(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Count characters in s1
        s1_count, window_count = [0] * 26, [0] * 26
        for right in range(len(s1)):
            s1_count[ord(s1[right]) - ord("a")] += 1
            window_count[ord(s2[right]) - ord("a")] += 1

        if window_count == s1_count:
            return True

        # Slide the window
        left = 0
        for right in range(len(s1), len(s2)):
            window_count[ord(s2[left]) - ord("a")] -= 1
            window_count[ord(s2[right]) - ord("a")] += 1
            if window_count == s1_count:
                return True
            left += 1

        return False

    # Time: O(n)
    # Space: O(1)
    def matches(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count, window_count = [0] * 26, [0] * 26
        for right in range(len(s1)):
            s1_count[ord(s1[right]) - ord("a")] += 1
            window_count[ord(s2[right]) - ord("a")] += 1

        matches = 0
        for ch in range(26):
            matches += s1_count[ch] == window_count[ch]

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[right]) - ord("a")
            window_count[index] += 1
            if window_count[index] == s1_count[index]:
                matches += 1
            elif window_count[index] == s1_count[index] + 1:
                matches -= 1

            index = ord(s2[left]) - ord("a")
            window_count[index] -= 1
            if window_count[index] == s1_count[index]:
                matches += 1
            elif window_count[index] == s1_count[index] - 1:
                matches -= 1
            left += 1

        return matches == 26

    def main(self):
        s1 = "ab"
        s2 = "eidbaooo"
        funcs = [self.array, self.matches]
        for func in funcs:
            start_time = timeit.default_timer()
            print(func(s1, s2))
            end_time = timeit.default_timer()
            print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds.")


if __name__ == "__main__":
    checkInclusion().main()
