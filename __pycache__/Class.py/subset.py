def subset_sum(nums, target):
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    # Base case initialization
    for i in range(n + 1):
        dp[i][0] = True

    # Build DP table
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

    # Backtrack to find subsets
    subsets = []
    def backtrack(i, j, subset):
        if i == 0 and j == 0:
            subsets.append(subset)
            return
        if i == 0 or j == 0:
            return
        if nums[i - 1] <= j:
            if dp[i - 1][j - nums[i - 1]]:
                backtrack(i - 1, j - nums[i - 1], [nums[i - 1]] + subset)
        if dp[i - 1][j]:
            backtrack(i - 1, j, subset)

    backtrack(n, target, [])

    return dp[n][target], subsets

# Example usage:
nums = [1,2,5,6,8] 
target = 9
found, subsets = subset_sum(nums, target)
if found: 
    print("Subset with sum {} found:".format(target))
    for subset in subsets:
        print(subset)
else:
    print("No subset with sum {} found.".format(target))