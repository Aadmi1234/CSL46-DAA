def merge(lst, low, mid, high):
    i = low
    j = mid+1
    k = 0
    temp = [0 for x in range(high-low+1)]
    # Merge two sorted subarrays into a temporary array
    while i <= mid and j <= high:
        if lst[i] <= lst[j]:
            temp[k] = lst[i]
            k += 1
            i += 1
        else:
            temp[k] = lst[j]
            j += 1
            k += 1

    # Copy the remaining elements from the first subarray, if any
    while i <= mid:
        temp[k] = lst[i]
        i += 1
        k += 1

    # Copy the remaining elements from the second subarray, if any
    while j <= high:
        temp[k] = lst[j]
        j += 1
        k += 1

    # Copy the sorted elements from the temporary array back to the original list
    for i in range(low, high+1):
        lst[i] = temp[i-low]

def mergeSort(lst, low, high):
    # Base case: If the list has more than one element
    if low < high:
        mid = (low + high) // 2
        # Recursively sort the two halves
        mergeSort(lst, low, mid)
        mergeSort(lst, mid+1, high)
        merge(lst, low, mid, high)

if __name__ == "__main__":
    lst = [1, 2, 6, 4, 5 , 8, 7, 3]

    print("Unsorted list : ")
    print(lst)

    b = mergeSort(lst, 0, len(lst)-1)

    print("Sorted list : ")
    print(lst)


"""
Output:
Unsorted list : 
[1, 2, 6, 4, 5, 8, 7, 3]
Sorted list : 
[1, 2, 3, 4, 5, 6, 7, 8]
"""

"""
Tc : O(nlogn)
SC : O(n)  # for the temp array we are using
"""
