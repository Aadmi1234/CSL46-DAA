def wis(requests):
    requests.sort(key=lambda x: x[1]) #sort the request based on their finish time

    N = len(requests)
    dp = [0] * (N + 1) # list will be used for dynamic programming to store intermediate results with all intialized to 0 of size n

    for i in range(1, N + 1):# iterate i from 1 to n(here 6)
        j = i - 1
        while j >= 0 and requests[j][1] > requests[i-1][0]: # while finish time of jth request is greater than start time of current request
            dp[i] = max(requests[i-1][2] + dp[j], dp[i-1]) # update the dp
            j -= 1
    return dp[N]


# requests are of the form (start_time, finish_time, value)
requests = [
    (1, 2, 100),
    (2, 5, 200),
    (3, 6, 300),
    (4, 8, 400),
    (5, 9, 500),
    (6, 10, 100)
    ]
max_profit = wis(requests)
print(f"Maximum profit: {max_profit}")


"""
-------------------------------------

Output:-
Maximum profit: 800

-------------------------------------
Applications:

Job Scheduling: In job scheduling scenarios, such as in a computing cluster or server farm, weighted interval scheduling can be used to allocate resources efficiently. Each job represents an interval with a weight indicating its priority or significance. By selecting a subset of non-overlapping jobs with high weights, system administrators can prioritize critical tasks and optimize resource utilization.

Resource Allocation: Weighted interval scheduling can also be applied to allocate limited resources, such as meeting rooms, vehicles, or equipment, among different users or groups. By assigning weights to the intervals representing resource requests, the scheduling algorithm can optimize resource usage and satisfy high-priority requests.

-------------------------------------

Time Complexity:
The time complexity is O(nlogn) for all the cases.
The overall time complexity of the algorithm can be analyzed as follows:

Sorting: O(n log n)
Dynamic programming loop: For each i iteration (from 1 to n), the nested while loop can iterate up to i times. Since the nested loop iterates up to n times in total, the time complexity of the nested loop is O(n).
Hence, the overall time complexity of the algorithm is O(n log n) + O(n), which can be simplified to O(n log n) since the sorting dominates the overall time complexity.
__________________________________________________________________________________________________________________________________________________________________

"""
