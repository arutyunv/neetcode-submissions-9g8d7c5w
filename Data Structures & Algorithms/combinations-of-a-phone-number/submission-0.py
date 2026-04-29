### Backtracking Approach ###

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Final answer:
        # This will store all complete letter combinations
        res = []

        # Mapping from digit -> possible letters
        # Same mapping as on a phone keypad
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        # Backtracking helper
        # i = current index in the digits string
        # curStr = current string we are building
        def backtrack(i, curStr):

            # Base case:
            # If current string length matches input length,
            # we have chosen one letter for every digit
            if len(curStr) == len(digits):
                # Save completed combination
                res.append(curStr)
                return

            # Get all possible letters for current digit
            # Example: digits[i] = "2" -> "abc"
            for c in digitToChar[digits[i]]:

                # Choose current letter c
                # Move to next digit (i + 1)
                backtrack(i + 1, curStr + c)

        # Edge case:
        # Only start backtracking if input is not empty
        if digits:
            backtrack(0, "")

        # Return all possible letter combinations
        return res


        