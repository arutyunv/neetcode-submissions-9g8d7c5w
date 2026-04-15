### Horizontal Scanning ###

# Start with the first string as the initial prefix candidate. 
# Then compare it with each subsequent string, shrinking the prefix to match only the common portion. 
# After processing all strings, what remains is the longest common prefix. 
# The prefix can only shrink or stay the same as we go through more strings.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Start by assuming the whole first string is the common prefix
        prefix = strs[0]

        # Compare this prefix with every other string in the list
        for i in range(1, len(strs)):
            j = 0  # pointer to compare characters

            # Compare characters one by one
            # Stop when we reach the end of either string
            while j < min(len(prefix), len(strs[i])):
                # If characters don't match, stop comparison
                if prefix[j] != strs[i][j]:
                    break
                # Move to next character
                j += 1

            # After comparison, keep only the matching part
            # This shrinks the prefix
            prefix = prefix[:j]

        # After checking all strings, prefix is the answer
        return prefix