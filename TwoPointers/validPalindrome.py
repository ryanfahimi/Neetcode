import timeit
import re


class validPalindromes:
    # Time: O(n)
    # Space: O(n)
    def regex(self, s: str) -> bool:
        s = re.sub("[^a-zA-Z0-9]", "", s).lower()
        return s == s[::-1]

    # Time: O(n)
    # Space: O(n)
    def filter_and_compare(self, s: str) -> bool:
        # Filter out non-alphanumeric characters and convert to lowercase
        s = "".join(char for char in s if char.isalnum()).lower()
        # Compare s with its reverse
        return s == s[::-1]

    # Time: O(n)
    # Space: O(1)
    def two_pointers(self, s: str) -> bool:
        # Two pointers
        left, right = 0, len(s) - 1
        while left < right:
            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def main(self):
        s = "A man, a plan, a canal: Panama"
        funcs = [self.regex, self.filter_and_compare, self.two_pointers]
        for func in funcs:
            start_time = timeit.default_timer()
            print(func(s))
            end_time = timeit.default_timer()
            print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds.")


if __name__ == "__main__":
    validPalindromes().main()
