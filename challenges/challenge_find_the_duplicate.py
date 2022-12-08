def find_duplicate(nums):
    nums.sort()
    if len(nums) <= 1:
        return False
    for index in range(len(nums)-1):
        num = nums[index]
        if not isinstance(num, int) or num <= 0:
            return False
        if num == nums[index + 1]:
            return num
    return False
