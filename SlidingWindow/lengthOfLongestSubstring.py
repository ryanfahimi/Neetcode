import timeit


class lengthOfLongestSubstring:
    # Time: O(n)
    # Space: O(n)
    def hash_table(self, s: str) -> int:
        # Create a dictionary to store the characters and their indices
        char_dict = {}
        # Initialize the start of the window and the maximum length
        left, max_length = 0, 0
        for right in range(len(s)):
            # If the character is in the dictionary
            if s[right] in char_dict:
                # Update the start of the window
                left = max(left, char_dict[s[right]] + 1)
            # Add the character and its index to the dictionary
            char_dict[s[right]] = right
            # Update the maximum length
            max_length = max(max_length, right - left + 1)
        return max_length

    # Time: O(n)
    # Space: O(n)
    def hash_set(self, s: str) -> int:
        # Create a set to store the characters
        char_set = set()
        # Initialize the start of the window and the maximum length
        left, max_length = 0, 0
        for right in range(len(s)):
            # If the character is in the set
            while s[right] in char_set:
                # Remove the character at the start of the window
                char_set.remove(s[left])
                # Update the start of the window
                left += 1
            # Add the character to the set
            char_set.add(s[right])
            # Update the maximum length
            max_length = max(max_length, right - left + 1)
        return max_length

    def main(self):
        s = "abcabcdbb"
        funcs = [self.hash_table, self.hash_set]
        for func in funcs:
            start_time = timeit.default_timer()
            print(func(s))
            end_time = timeit.default_timer()
            print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds.")


if __name__ == "__main__":
    lengthOfLongestSubstring().main()
