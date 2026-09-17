
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    for j in range(len(nums)):
        # keep the element if we have written less than 2 items,
        # or if current element is different from the element at i-2
        if i < 2 or nums[j] != nums[i-2]:
            nums[i] = nums[j]
            i += 1
    return i


nums = [1, 1, 1, 2, 2, 3]
