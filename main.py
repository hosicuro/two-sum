def twoSum(nums: list[int], target: int) -> list[int]:
    nums.sort()
    i, j = 0, len(nums) - 1
    while i < j:
        if nums[i] + nums[j] == target:
            return [i, j]
        elif nums[i] + nums[j] > target:
            j -= 1
        else:
            i -= 1

arr = [2, 7, 11, 15]
num = 9
print(twoSum(arr, num))
