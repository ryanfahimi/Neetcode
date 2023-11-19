import timeit


class characterReplacement:
    # Time: O(n)
    # Space: O(1)
    def hash_table(self, s: str, k: int) -> int:
        # Create a dictionary to store the frequency of each character
        char_dict = {}
        # Initialize the left and right pointers
        left = 0
        # Initialize the max length
        max_length = 0
        # Iterate through the string
        for right in range(len(s)):
            # Add the character to the dictionary
            char_dict[s[right]] = char_dict.get(s[right], 0) + 1
            # Calculate the current length
            current_length = right - left + 1
            # If the current length minus the max count is greater than k
            if current_length - max(char_dict.values()) > k:
                # Decrement the frequency of the character at the left pointer
                char_dict[s[left]] -= 1
                # Increment the left pointer
                left += 1
            # Update the max length
            max_length = max(max_length, right - left + 1)
        return max_length

    # Time: O(n)
    # Space: O(1)
    def max_count(self, s: str, k: int) -> int:
        # Create a dictionary to store the frequency of each character
        char_dict = {}
        # Initialize the left and right pointers
        left = 0
        # Initialize the max count and max length
        max_count = max_length = 0
        # Iterate through the string
        for right in range(len(s)):
            # Add the character to the dictionary
            char_dict[s[right]] = char_dict.get(s[right], 0) + 1
            # Update the max count
            max_count = max(max_count, char_dict[s[right]])
            # Calculate the current length
            current_length = right - left + 1
            # If the current length minus the max count is greater than k
            if current_length - max_count > k:
                # Decrement the frequency of the character at the left pointer
                char_dict[s[left]] -= 1
                # Increment the left pointer
                left += 1
            # Update the max length
            max_length = max(max_length, right - left + 1)
        return max_length

    def main(self):
        s = "ABAB"
        k = 2
        funcs = [self.hash_table, self.max_count]
        for func in funcs:
            start_time = timeit.default_timer()
            print(func(s, k))
            end_time = timeit.default_timer()
            print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds.")


if __name__ == "__main__":
    characterReplacement().main()
