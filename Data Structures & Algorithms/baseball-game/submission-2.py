class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Step 1. Initialize stack 
        stack = [] 

        # Step 2. Go over all operations in list of operations 
        for op in operations:
            # Write out if statements 
            if op == "+":
                # add last and second to last value, append to the stack (push op)
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                # get last value, double it and append to the stack (push op)
                stack.append(stack[-1]*2)
            elif op == "C":
                # popping a value / removing the last element
                stack.pop()
            else: # we have a number that we need to add 
                # convert string value to int type, and append it / push to stack
                stack.append(int(op))

        # take sum of the stack
        return sum(stack)