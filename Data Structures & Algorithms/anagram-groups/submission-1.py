### Sorting Approach ###

# Anagrams become identical when their characters are sorted.
# For example, "eat", "tea", and "ate" all become "aet" after sorting.
# By using the sorted version of each string as a key, we can group all anagrams together.
# Strings that share the same sorted form must be anagrams, so placing them in the same group is both natural and efficient.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a hash map 
        hash_map = {}

        # Loop over strings in strs array 
        for string in strs:
            # This is how string sorting is done:
            # "Break string into characters - sort - glue back together”
            sorted_str = "".join(sorted(string))
            
            # Check if this sorted string is in hash map
            if sorted_str in hash_map:
                # if so, append the string 
                hash_map[sorted_str].append(string)

                # if not, create a new key-value pair 
            else:
                hash_map[sorted_str] = [string]

        # After processing all strings, 
        # return all values from the hash map, which represent the grouped anagrams
        return list(hash_map.values())
        