### Vertical Scanning ### 

## Idea: Instead of comparing horizontally, we can compare characters column by column across all strings. 
# Check if all strings have the same character at position 0, then position 1. 
# The moment we find a mismatch or reach the end of any string, we have found where 
# the common prefix ends. 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Initialize min_len with a large number
        # (we will find the shortest string length)
        min_len = 201

        # Loop through all strings to find the shortest one
        for string in strs:
            # If current string is shorter than what we have seen so far
            if len(string) < min_len:
                # Update minimum length
                min_len = len(string)
                # Store this shortest string
                min_string = string 
        
        # This will store the final common prefix
        prefix = ""

        # Loop through each character index of the shortest string
        # (we only need to check up to the shortest length)
        for j in range(len(min_string)):

            # Compare this character with ALL strings
            for i in range(len(strs)): 
                # If any string has a different character at position j
                if strs[i][j] != min_string[j]:
                    # We stop immediately and return what we built so far
                    return prefix 

            # If all strings matched at position j,
            # add this character to the prefix
            prefix += min_string[j]

        # If we never broke early, the whole min_string is common prefix
        return prefix
            


        