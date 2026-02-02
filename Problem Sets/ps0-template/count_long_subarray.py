def count_long_subarray(A):
    """
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    """
    count = 1
    longest = 1
    current_count = 1

    for i in range(1, len(A)):
        if A[i] > A[i - 1]:
            current_count += 1
        else:
            current_count = 1
        if current_count == longest:
            count += 1
        elif current_count > longest:
            longest = current_count
            count = 1

    return count


result = count_long_subarray(
    (4, 18, 10, 8, 13, 16, 18, 1, 9, 6, 11, 13, 12, 5, 7, 17, 13, 3)
)
print(result)
