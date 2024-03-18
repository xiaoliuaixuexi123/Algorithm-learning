from random import randint


def insertion_sort(arr: list[int]):
    for i in range(1, len(arr)):
        base = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > base:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = base


if __name__ == '__main__':
    nums = [randint(0, 100) for _ in range(100)]
    print(nums)
    insertion_sort(nums)
    print(nums)