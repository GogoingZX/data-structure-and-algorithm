def binary_search(sorted_seq, val):
    low = 0
    high = len(sorted_seq) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_seq[mid] == val:
            return mid
        elif sorted_seq[mid] > val:
            high = mid - 1
        else:
            low = mid + 1
    return low

#---------------------------------------------------------------------------------------------------
l1 = [1, 2, 3, 6, 9, 12, 22, 33, 40, 50, 52]
assert binary_search(l1, 6) == 3
print("OK")