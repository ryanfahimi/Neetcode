from typing import List


class lengthOfLongestSubstring:
    def sliding_window(self, s: str) -> int:
        # Create a dictionary to store the characters and their indices
        char_dict = {}
        # Initialize the start of the window and the maximum length
        start, max_length = 0, 0
        for end in range(len(s)):
            # If the character is in the dictionary
            if s[end] in char_dict:
                # Update the start of the window
                start = max(start, char_dict[s[end]] + 1)
            # Add the character and its index to the dictionary
            char_dict[s[end]] = end
            # Update the maximum length
            max_length = max(max_length, end - start + 1)
        return max_length

    def main(self):
        s = "abcabcbb"
        print(self.sliding_window(s))


if __name__ == "__main__":
    lengthOfLongestSubstring().main()
