# valid parentheses
# Given a string s containing : ( ) { } [ ] 
#  Return true if the string is valid
# A string is valid if every opening bracket has a matching closing bracket
# or they close in the correct order

def is_valid(s):
    # create a stack to keep track of opening brackets
    stack = []
    # mapping dictionary
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    # Loop through the string
    for char in s:
        if char in "({[":
            # if the character is an an open bracket, push itto the stack
            stack.append(char)
        else:
            # else, the character is a closing bracket
            if not stack:
                #if the stack is empty, then we have a closing bracket
                return False
            last = stack[-1] # get the last opening bracket from the stack

            if pairs[char] == last:
                # if the last opening bracket matches the current closing bracket, pop it from the stack
                stack.pop()

    # if the stack is empty at the end, then all brackets are valid
    return len(stack) == 0

# test case 
if __name__ == "__main__":
    s = "({[]})"
    x = "(()"
    result = is_valid(s)
    result2 = is_valid(x)
    print(result)  # Output: True
    print(result2)  # Output: False
    if result == True and result2 == False:
        print("Test case passed!")    
    else:
        print("Test case failed!")
