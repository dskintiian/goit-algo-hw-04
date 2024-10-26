from timeit import timeit
from random import sample

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >=0 and key < data[j] :
                data[j + 1] = data[j]
                j -= 1
        data[j + 1] = key
    return data

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def test_sorting_algo(data: list):
    print(f'Size: {len(data)}; sort(); {timeit(lambda: data.sort(), number=10000)}')
    print(f'Size: {len(data)}; sorted(); {timeit(lambda: sorted(data), number=10000)}')
    print(f'Size: {len(data)}; insertion_sort(); {timeit(lambda: insertion_sort(data), number=10000)}')
    print(f'Size: {len(data)}; merge_sort(); {timeit(lambda: merge_sort(data), number=10000)}')

if __name__ == '__main__':
    for size in [10,100,1000,10000,100000]:
        test_sorting_algo(sample(range(1, size*100), size))
