# Theetta_sort
def Theetta_sort(A, k):
    n = len(A)
    C = [0] * (k + 1)
    B = [0] * (k + 1)

    for i in range(n):
        B[A[i]] += 1
        C[A[i]] += 1


    for i in range(1, k + 1):
        B[i] += B[i - 1]

    j = n - 1
    while j >= 0:
        if C[A[j]] > 0:
            C[A[j]] -= 1
            if B[A[j]] != j + 1:
                pos = B[A[j]] - 1
                B[A[j]] -= 1
                A[j], A[pos] = A[pos], A[j]

            else:
                B[A[j]] -= 1
                j -= 1
        else:
            j -= 1

    return A


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]   # Left half
        R = arr[mid:]   # Right half

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Merge two halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy remaining elements
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def quick_sort(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            i += 1
            arr[i], arr[high] = arr[high], arr[i]

            # Push subarrays to stack
            stack.append((low, i - 1))
            stack.append((i + 1, high))
    return arr



import time
import random


original_array = [random.randint(1, 10000) for _ in range(10000000)]

# Bubble Sort
# arr1 = original_array.copy()
# start = time.time()
# bubble_sort(arr1)
# end = time.time()
# print("Bubble Sort Time:", end - start)

# Insertion Sort
# arr2 = original_array.copy()
# start = time.time()
# insertion_sort(arr2)
# end = time.time()
# print("Insertion Sort Time:", end - start)

# Merge Sort
arr3 = original_array.copy()
start = time.time()
merge_sort(arr3)
end = time.time()
print("Merge Sort Time:", end - start)

#Quick Sort
arr4 = original_array.copy()
start = time.time()
quick_sort(arr4)
end = time.time()
print("Quick Sort Time:", end - start)


# Theetta Sort
arr5 = original_array.copy()
start = time.time()
T = Theetta_sort(arr5, max(arr5))
end = time.time()
print("Theetta Sort Time:", end - start)

