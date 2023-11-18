import timeit
import re


class validPalindromes:
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
        funcs = [self.two_pointers]
        for func in funcs:
            start_time = timeit.default_timer()
            print(func(s))
            end_time = timeit.default_timer()
            print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds.")


if __name__ == "__main__":
    validPalindromes().main()
