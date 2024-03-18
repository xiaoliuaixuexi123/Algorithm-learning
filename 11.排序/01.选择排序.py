from random import randint


def selection_sort(arr: list):
    num = len(arr)
    for i in range(num - 1):
        k = i
        for j in range(i + 1, num):
            if arr[j] < arr[k]:
                k = j
        arr[i], arr[k] = arr[k], arr[i]


if __name__ == '__main__':
    random_list = [randint(0, 100) for _ in range(100)]
    print(random_list)
    selection_sort(random_list)
    print(random_list)
