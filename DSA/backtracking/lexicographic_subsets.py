def lexicographic_subsets(arr):
    arr.sort()  # Make sure it's in ascending order
    result = []
    
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result

# Example usage
S = [1, 2, 3]
for subset in lexicographic_subsets(S):
    print(subset)
