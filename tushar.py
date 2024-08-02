def backtrack_subset_sum(nums, target, index, path, result):
    if target == 0:
        result.append(path[:])  # Append a copy of the current subset to the result
        return
    if target < 0 or index >= len(nums):
        return
    
    # Include the current number in the subset
    path.append(nums[index])
    backtrack_subset_sum(nums, target - nums[index], index + 1, path, result)
    
    # Exclude the current number from the subset
    path.pop()
    backtrack_subset_sum(nums, target, index + 1, path, result)

def subset_sum(nums, target):
    result = []
    backtrack_subset_sum(nums, target, 0, [], result)
    return result

# Example usage:
numbers = [2, 4, 6, 8]
target_sum = 10
subsets = subset_sum(numbers, target_sum)
print("Subsets with sum", target_sum, "are:", subsets)