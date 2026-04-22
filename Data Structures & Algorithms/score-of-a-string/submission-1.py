### Brute Force Approach ### 

"""
Just iterate over each pair of adjacent characters, find their ascii representation, find their abs difference, ans sum up. 

Return the final sum/score. 

"""

class Solution:
    def scoreOfString(self, s: str) -> int:
        # Initialize score variable that will be returned
        score = 0 

        # Loop over every character in the string except for the last one
        for i in range(len(s)-1): 
            # Get the ASCII codes of the two adjacent characters 
            ascii1 = ord(s[i])
            ascii2 = ord(s[i+1])
            # Calculate current absolute difference and add to the total score count
            score+= abs(ascii1 - ascii2)
        return score 


        