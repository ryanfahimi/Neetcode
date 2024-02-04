import timeit


class minWindow:
    def brute_force(self, s: str, t: str) -> str:
        # Create a dictionary to store the frequency of each character
        t_count, window_count = {}, {}
        # Iterate through the characters in t
        for ch in t:
            # Add the count of the character to t_count
            t_count[ch] = t_count.get(ch, 0) + 1

        left = 0
        min_length = float("inf")
        result = ""

        # Iterate through the indeces of the characters in s
        for right in range(len(s)):
            # Add the count of the character to window_count
            window_count[s[right]] = window_count.get(s[right], 0) + 1
            # While the window contains all the characters in t
            while left <= right and all(
                window_count.get(char, 0) >= count for char, count in t_count.items()
            ):
                # Update the result if the current window is smaller than the minimum window
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = s[left : right + 1]
                # Remove the count of the character from window_count
                window_count[s[left]] -= 1
                left += 1

        return result

    def hash_table(self, s: str, t: str) -> str:
        # Create a dictionary to store the frequency of each character
        t_count, window_count = {}, {}
        # Iterate through the characters in t
        for ch in t:
            # Add the count of the character to t_count
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
            # Add the count of the character to window_count
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

                # Remove the count of the character from window_count
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
        funcs = [self.brute_force, self.hash_table]
        for func in funcs:
            start_time = timeit.default_timer()
            print(func(s, t))
            end_time = timeit.default_timer()
            print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds.")


if __name__ == "__main__":
    minWindow().main()
