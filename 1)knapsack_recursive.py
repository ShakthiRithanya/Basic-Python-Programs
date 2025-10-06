# Enhanced 0/1 Knapsack using recursion + memoization

def knapsack_recursive(wt, val, W, n, memo=None):
    # Initialize memoization dictionary
    if memo is None:
        memo = {}
    
    # Base condition
    if n == 0 or W == 0:
        return 0

    # Check if result is already computed
    if (n, W) in memo:
        return memo[(n, W)]

    # If weight of current item <= remaining capacity
    if wt[n - 1] <= W:
        include_item = val[n - 1] + knapsack_recursive(wt, val, W - wt[n - 1], n - 1, memo)
        exclude_item = knapsack_recursive(wt, val, W, n - 1, memo)
        memo[(n, W)] = max(include_item, exclude_item)
    else:
        # If weight of current item is more than capacity
        memo[(n, W)] = knapsack_recursive(wt, val, W, n - 1, memo)

    return memo[(n, W)]


# Example usage
if __name__ == "__main__":
    weights = [1, 2, 3, 6]
    values = [1, 2, 4, 6]
    capacity = 6
    n = len(weights)

    max_value = knapsack_recursive(weights, values, capacity, n)
    print(f"Maximum value that can be obtained = {max_value}")
