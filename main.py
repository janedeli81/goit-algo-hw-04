import timeit
import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def generate_random_array(n):
    return [random.randint(0, n) for _ in range(n)]


def generate_almost_sorted_array(n):
    arr = list(range(n))
    for _ in range(int(n * 0.05)):  # Змінюємо 5% елементів
        arr[random.randint(0, n - 1)] = random.randint(0, n)
    return arr


def generate_reverse_sorted_array(n):
    return list(range(n, 0, -1))


def measure_sorting_time(sort_func, arr):
    start_time = timeit.default_timer()
    sort_func(arr.copy())
    end_time = timeit.default_timer()
    return end_time - start_time


sizes = [100, 1000, 5000]
sort_functions = {"Insertion Sort": insertion_sort, "Merge Sort": merge_sort, "Timsort (sorted())": sorted}

for size in sizes:
    print(f"\nArray size: {size}")
    random_array = generate_random_array(size)
    almost_sorted_array = generate_almost_sorted_array(size)
    reverse_sorted_array = generate_reverse_sorted_array(size)
    for name, func in sort_functions.items():
        print(f"{name}:")
        for arr_type, arr in [("Random", random_array), ("Almost Sorted", almost_sorted_array),
                              ("Reverse Sorted", reverse_sorted_array)]:
            time = measure_sorting_time(func, arr)
            print(f"  {arr_type} array sort time: {time:.6f} seconds")
