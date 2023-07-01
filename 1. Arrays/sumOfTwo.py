# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

new_arr = []


def get_subarrys(nums, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if target == nums[i]+nums[j]:
                new_arr.extend((i, j))
    return new_arr


arr = [2, 7, 3, 9, 11, -2, 15, 8, 5, 4, 0, 1, 6]
target = 9
print(get_subarrys(arr, target))
