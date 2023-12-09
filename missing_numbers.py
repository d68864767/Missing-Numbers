def findMissingIDs(n, ids):
    # Create a boolean array to mark the IDs that exist
    exists = [False] * (n + 1)

    # Mark the IDs that exist
    for id_num in ids:
        exists[id_num] = True

    # Find and collect the missing IDs
    missing_ids = [i for i in range(1, n + 1) if not exists[i]]

    return missing_ids

# Example usage:
# missing_ids = findMissingIDs(5, [2, 3, 4, 5])
# print(missing_ids)  # Output should be [1]
