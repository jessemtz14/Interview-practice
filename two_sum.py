# Two sum

def two_sum(nums, target):
    # create a dictionary to store the indices and the numbers we have seen
    seen = {}

    # loop through the list of numbers, but we have to enumerate it to
    # get the index of the number as well
    for index, num in enumerate(nums):
        # get the complement of the current number
        need = target - num
        # check if the complement is in the dictionary
        if need in seen:
            # if it is, we have found the two numbers that add up to the target
            return [seen[need], index]
        seen[num] = index # add the current number and its index to the dictionary

    return [None, None]  # return None if no solution is found

# test case
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(result)  # Output: [0, 1]
    if result == [0, 1]:
        print("Test case passed!")    
    else:
        print("Test case failed!")
