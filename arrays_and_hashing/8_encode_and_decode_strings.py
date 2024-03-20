from typing import List

# 659. Encode and Decode Strings
# Medium

# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]


# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.


class Solution:

    # Time: O(n)
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            # The length of the string is converted to a string and concatenated with a colon and the string itself.
            # The resulting list of encoded strings is then joined into a single string with no separator.
            encoded_str += str(len(s)) + ":" + s
        return encoded_str

    # Time: O(n)
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            # The index is updated to the start of the next string.
            j = i

            # Find the colon that separates the length of the string and the string itself.
            while s[j] != ":":
                j += 1

            # The length of the string is extracted and converted to an integer.
            length = int(s[i:j])

            # The index is then updated to the end of the string.
            i = j + 1 + length

            # The string is then extracted using the length and added to the result list.
            decoded_strs.append(s[j + 1 : i])
        return decoded_strs

    def main(self):
        strs = ["neet", "code", "love", "you"]
        print(f"Input: {strs}")
        print(f"Output: {self.decode(self.encode(strs))}")

        strs = ["we", "say", ":", "yes"]
        print(f"Input: {strs}")
        print(f"Output: {self.decode(self.encode(strs))}")


if __name__ == "__main__":
    Solution().main()
