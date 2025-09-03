#1. Bubble Sort -- Easy but slow (O(n²))

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        #last i element are already in place
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                #swap if the element is greater than the next one
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#Example:

arr = [64, 25, 12, 22, 11]
print("Unsorted array:", arr)
sorted_arr = bubblesort(arr)
print("Sorted array:", sorted_arr)

#2. Quick Sort -- Fast on average (O(n log n)), but worst case O(n²)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] #choosing the middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

#Example:
qs_arr = [64, 25, 12, 22, 11]
unsorted_qs_arr = print("Unsorted list:", qs_arr)
sorted_qs_arr = print("Sorted Quick Sort:", quick_sort(qs_arr))





#3. Merge Sort -- Always O(n log n), but uses extra memory
"""
Merge Sort is a divide and conquer algorithm:

    1. Divide the array into halves recursively.
    2. Sort each half.
    3. Merge the sorted halves.
"""

def merge_sort(arr):
    if (len(arr) <= 1):
        return arr
    mid = len(arr)//2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    #compare elements and merge in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    #add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

#Example

ms_arr = [64, 25, 12, 22, 11 ]
unosrted_qsarr = print("Unsorted list:", ms_arr)
merged_sort = print("Merged sort result:", merge_sort(ms_arr))