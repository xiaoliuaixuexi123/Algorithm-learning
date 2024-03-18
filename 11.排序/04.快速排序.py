from random import randint


def partition(nums: list[int], left: int, right: int):
    """哨兵分化"""
    """以nums[left]为基准数"""
    i, j = left, right
    while i < j:
        while i < j and nums[i] <= nums[left]:
            i += 1  # 从左向右找首个大于基准数的元素
        while i < j and nums[j] >= nums[left]:
            j -= 1  # 从右向左找首个小于基准数的元素
        # 元素交换
        nums[j], nums[i] = nums[i], nums[j]
    # 将基准数交换到两子数组的分界线
    nums[i], nums[left] = nums[left], nums[i]
    return i  # 返回基准数组索引


def quick_sort(self, nums: list[int], left: int, right: int):
    """快速排序"""
    # 子数组长度为 1 时终止递归
    if left >= right:
        return
    # 哨兵划分
    pivot = self.partition(nums, left, right)
    # 递归左子数组、右子数组
    self.quick_sort(nums, left, pivot - 1)
    self.quick_sort(nums, pivot + 1, right)



if __name__ == '__main__':
    arr = [randint(0, 100) for _ in range(100)]
    print(arr)
    quick_sort(arr)
    print(arr)
