def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted
        j = i - 1  # Index of the previous element

        # Move elements of arr[0...i-1] that are greater than the key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  # Place the key at its correct position in the sorted subarray

# Driver Code
array=[]
n=int(input("Enter the no of elements: "))
print("Enter the elements: ")
for i in range(n):
    array.append(int(input()))

insertion_sort(array)
print("The array after sorting:")
print(array)


"""
----------------------------------------------------------------------------------------------------
Output:

Enter the no of elements: 5
Enter the elements: 
3
5
63
2
43
The array after sorting:
[2, 3, 5, 43, 63]
----------------------------------------------------------------------------------------------------

APPLICATIONS of Insertion Sort:

Small Input Sizes: Insertion Sort performs efficiently on small input sizes or partially sorted arrays where the number of elements is relatively small. Its simplicity and ease of implementation make it suitable for such cases.

Partially Sorted Arrays: If an array is partially sorted or has a small number of elements out of order, Insertion Sort can efficiently sort it. In such cases, the number of comparisons and shifts required is relatively small, resulting in a faster sorting process compared to other algorithms.

Online Sorting: Insertion Sort is well-suited for online sorting scenarios where new elements are continuously added to the existing sorted list. It can efficiently insert the new elements at their appropriate positions, maintaining the sorted order.

----------------------------------------------------------------------------------------------------

TIME COMPLEXITY of Insertion Sort:
The time complexity of Insertion Sort is O(n^2) in the worst case and average case, where n is the number of elements in the array. 
However, in the best case scenario, when the array is already sorted, the time complexity reduces to O(n). 
"""
