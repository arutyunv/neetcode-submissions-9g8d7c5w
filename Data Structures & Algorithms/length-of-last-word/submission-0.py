### Brute Force Approach ###

"""
Scanning from the end is more direct since we only care about the last word. 
First skip any trailing spaces, then count characters until we hit a space or the beginning of the string.
This avoids processing earlier parts of the string entirely. 
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Get the last index and init length to 0 
        i, length = len(s) - 1, 0
        # Skip any trailing spaces at the end
        # by skipping, we move the pointer/index backwards to the beginning 
        while s[i] == ' ':
            i -= 1
        # count real characters 
        while i >= 0 and s[i] != ' ':
            i -= 1
            length += 1
        return length

        