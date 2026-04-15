### Hash Map Approach ### 

## Idea: f two strings are anagrams, they must use the same characters with the same frequencies.
# By using two hash maps (or dictionaries), we track the frequency of every character in each string.
# f both frequency maps match exactly, then the strings contain the same characters with same frequencies, meaning they are anagrams.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the strings have different lengths,
        # they CANNOT be anagrams
        if len(s) != len(t):
            return False 

        # Create two hash maps (dictionaries)
        # to count how many times each character appears
        hashmap_for_s = {}
        hashmap_for_t = {}

        # Loop through both strings at the same time
        for i in range(len(s)):
            # For string s:
            # Get current count of character s[i] (default 0 if not present)
            # Add 1 and store it back
            hashmap_for_s[s[i]] = 1 + hashmap_for_s.get(s[i], 0)

            # Do the same for string t
            hashmap_for_t[t[i]] = 1 + hashmap_for_t.get(t[i], 0)
        
        # Finally, compare both hash maps
        # If they are equal, then same characters with same frequencies
        # so strings are anagrams
        return hashmap_for_s == hashmap_for_t


        
        