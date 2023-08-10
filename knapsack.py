def knapsack(weight, value, W, N):
    # 2-D array to store the intermediate values
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

    # weight and value list have 0-based indexing
    # dp has one based indexing
    # therefore we subtract 1 to access the indexes of weight and value

    for i in range(1, N+1):
        for w in range(1, W+1):
            if(weight[i-1] > w):
                dp[i][w] = dp[i-1][w]
            else :
                dp[i][w] = max(dp[i-1][w] , dp[i-1][w - weight[i-1]] + value[i-1])

    # Now let's find the items chosen for the knapsack
    i = N
    j = W
    indOfItems = []

    while i>0 and j>0:
        if dp[i][j] != dp[i-1][j]:
            # This item was selected
            indOfItems.append(i-1)
            j = j - weight[i-1]
        i -= 1
        
    return dp[N][W], indOfItems


if __name__ == "__main__":
    weight = [3, 5, 6, 2]
    value = [10, 4, 9, 11]
    W = 7
    N = 4

    maxProfit, sol = knapsack(weight, value, W, N)

    # Printing out the solution
    print("The max profit = ", maxProfit)
    print("Items included: ")
    print("Weight \t Value")
    for i in sol:
        print(f"{weight[i]} \t {value[i]}")


"""
Output:

The max profit =  21
Items included: 
Weight 	 Value
2 	 11
3 	 10
"""

"""
TC : O(N*W)
SC : O(N*W)
"""
