def partition(a,low,high):
    
    """
    Rearranges the array such that all elements smaller than the pivot are on the left
    and all elements greater than the pivot are on the right.
    """
    
    pivot=a[low]
    p=low+1  #pointer for elements < pivot (left subarray)
    q=high   #pointer for elements > pivot (right subarray)
    while True:
        while p<=q and a[p]<=pivot:
            p+=1                     # pointer p is incremented as long as the element<pivot
        while p<=q and a[q]>pivot:
            q-=1                     # pointer q is decremented as long as the element>pivot
            
        if p<=q:                     # now p points to an element>pivot and q points to an element < pivot
            a[p],a[q]=a[q],a[p]      # the positions of these elements are swapped
        else:
            break
    a[low],a[q]=a[q],a[low]          # the pivot element is placed in its correct position
    return q

def quicksort(a,low,high):
    if(low<high):
        pivot=partition(a,low,high)   # Partition the array
        quicksort(a,low,pivot-1)      # Recursively sort the left subarray
        quicksort(a,pivot+1,high)     # Recursively sort the right subarray


# Driver Code
array=[]
n=int(input("Enter the no of elements: "))
print("Enter the elements: ")
for i in range(n):
    array.append(int(input()))
low=0
high=n-1
quicksort(array,low,high)
print("The array after sorting:")
print(array)

"""
----------------------------------------------------------------------------------------------------
Output:-

Enter the no of elements: 5
Enter the elements: 
2
32
1
3
5
The array after sorting:
[1, 2, 3, 5, 32]

----------------------------------------------------------------------------------------------------
APPLICATIONS of Quicksort:

General Sorting: Quicksort is widely used for sorting arrays or lists of elements in various programming languages and libraries due to its efficiency and simplicity.

Large Datasets: Quicksort performs well on large datasets, making it a popular choice for sorting large volumes of data efficiently.

In-Place Sorting: Quicksort operates on the input array itself, requiring only a small amount of additional memory for recursive calls. This makes it desirable in scenarios with limited memory availability.

Unstable Sorting: Quicksort is an unstable sorting algorithm, meaning it does not guarantee the relative order of equal elements after sorting. This property can be beneficial in certain applications where the original order of equal elements is not significant.

----------------------------------------------------------------------------------------------------
TIME COMPLEXITY of Quicksort:

The time complexity of Quicksort depends on the choice of the pivot and the partitioning strategy. In the average and best cases, Quicksort has a time complexity of O(n log n), where n is the number of elements in the array.

In the worst case, when the pivot is consistently chosen as the smallest or largest element, Quicksort can have a time complexity of O(n^2).
----------------------------------------------------------------------------------------------------
"""
