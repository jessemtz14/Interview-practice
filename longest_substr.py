# longest substring without repeating characters
# Given a string s, find the length of the longest substring
# without repeating characters

# example: 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def length_of_longest_substring(s):
    # create a set to store the characters in the window 
    seen = set()
    # create two variables to represent the window
    left = 0
    max_length = 0

    # loop through the string with the right pointer
    for right, char in enumerate(s):
        # if the character is in the set, we need to move the left pointer
        # until we remove the duplicate character from the set
        while char in seen: 
            # remove the character at the left pointer from the set
            seen.remove(s[left])
            # move left foreward 
            left += 1
        # add char to the set
        seen.add(char)
        # update the max length
        curr_length = right - left + 1
        max_length = max(max_length, curr_length)
    # return the max length
    return max_length


if __name__ == "__main__":
    s = "abcabcbb"
    result = length_of_longest_substring(s)
    print(result)  # Output: 3
    if result == 3:
        print("Test case passed!")    
    else:
        print("Test case failed!")

    s2 = "abbaacdef"
    result2 = length_of_longest_substring(s2)
    print(result2)  # Output: 5 "acdef"
    if result2 == 5:
        print("Test case passed!")
    else:
        print("Test case failed!")