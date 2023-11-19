import timeit


class minWindow:
    def brute_force(self, s: str, t: str) -> str:
        # Create a dictionary to store the frequency of each character
        t_count, window_count = {}, {}
        for ch in t:
            t_count[ch] = t_count.get(ch, 0) + 1

        left = 0
        min_length = float("inf")
        result = ""

        for right in range(len(s)):
            window_count[s[right]] = window_count.get(s[right], 0) + 1
            while left <= right and all(
                window_count.get(char, 0) >= count for char, count in t_count.items()
            ):
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = s[left : right + 1]

                window_count[s[left]] -= 1
                left += 1

        return result

    def hash_table(self, s: str, t: str) -> str:
        t_count, window_count = {}, {}
        for ch in t:
            t_count[ch] = t_count.get(ch, 0) + 1

        have = 0
        need = len(t_count)

        left = 0
        min_length = float("inf")
        result = ""
        for right in range(len(s)):
            window_count[s[right]] = window_count.get(s[right], 0) + 1
            if s[right] in t_count and window_count[s[right]] == t_count[s[right]]:
                have += 1

            while left <= right and have == need:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = s[left : right + 1]

                window_count[s[left]] -= 1
                if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                    have -= 1

                left += 1

        return result

    def main(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        funcs = [self.brute_force, self.hash_table]
        for func in funcs:
            start_time = timeit.default_timer()
            print(func(s, t))
            end_time = timeit.default_timer()
            print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds.")


if __name__ == "__main__":
    minWindow().main()
