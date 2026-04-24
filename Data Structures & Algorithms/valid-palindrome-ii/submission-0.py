### Two-Pointer Approach ###

"""
Instead of blindly trying every removal, we can be smarter. 
Use two pointers starting from both ends of the string and move them inward. 
As long as characters match, keep going. When we find a mismatch, we know exactly where the problem is. 
At this point, we have only two choices: remove the left character or remove the right character. 
We check if either choice results in a palindrome for the remaining substring.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Helper: check if the substring s[l..r] (inclusive) is a palindrome
        def is_pal_range(l: int, r: int) -> bool:
            # Compare characters from both ends moving toward the center
            while l < r:
                if s[l] != s[r]:  # Mismatch means this substring isn't a palindrome
                    return False
                l += 1
                r -= 1
            return True  # All pairs matched -> palindrome

        # Two-pointer scan from both ends of the original string
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:  # First mismatch found
                # Either skip the left (L) character or skip the right (R) character
                # If either resulting substring is a palindrome, the answer is True
                return is_pal_range(l + 1, r) or is_pal_range(l, r - 1)

            # Characters match -> tighten the window
            l += 1
            r -= 1

        # No mismatches found -> the string is already a palindrome
        return True
        