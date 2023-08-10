def merge(lst, low, mid, high):
    i = low
    j = mid+1
    k = 0
    invCount = 0
    temp = [0 for x in range(high-low+1)]
    # Merge two sorted subarrays into a temporary array
    while i <= mid and j <= high:
        if lst[i] <= lst[j]:
            temp[k] = lst[i]
            k += 1
            i += 1
        else:
            temp[k] = lst[j]
            invCount += (mid-i+1)  # Update inversion count
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

    return invCount


def mergeSort(lst, low, high):
    invCount = 0
    # Base case: If the list has more than one element
    if low < high:
        mid = (low + high) // 2
        # Recursively sort the two halves and count inversions
        invCount += mergeSort(lst, low, mid)
        invCount += mergeSort(lst, mid+1, high)
        invCount += merge(lst, low, mid, high)
    return invCount


lst = [1, 2, 6, 4, 5 , 8, 7, 3]
b = mergeSort(lst, 0, len(lst)-1)
print("Number of inversions:", b)

"""
----------------------------------------------------------------------------------------------------
Output:-
Number of inversions: 8
----------------------------------------------------------------------------------------------------
Tc : O(nlogn)
SC : O(n) , # for the temp array we are using

----------------------------------------------------------------------------------------------------
Real life applications:
1)Financial Data Analysis: Counting inversions can be useful in financial data analysis, such as detecting anomalous or irregular patterns in stock market trades or financial transactions.
2)Collaborative Filtering: In recommender systems, counting inversions can help identify similar user preferences or item rankings, allowing for more accurate recommendations.
3)Genome Analysis: In bioinformatics, counting inversions can provide insights into the evolutionary history of species by comparing genetic sequences.
4)Image Processing: In image analysis, counting inversions can be used for feature extraction or pattern recognition tasks, such as identifying objects with certain color or intensity variations.
5)Optimization Problems: Counting inversions can be utilized as a measure of distance or dissimilarity between solutions in optimization problems, allowing for the exploration of different search spaces.
----------------------------------------------------------------------------------------------------
"""
