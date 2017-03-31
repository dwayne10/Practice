def sortAndCount(nums, start, end):
    if end - start <= 1:
        return 0

    mid = start + (end - start) // 2

    left = sortAndCount(nums, start, mid)
    right = sortAndCount(nums, mid, end)

    overall = countMergeInversions(start, mid, end, nums)
    return left + right + overall


def countMergeInversions(start, mid, end, nums):
    i = start
    j = mid

    res = []
    count = 0
    while i < mid and j < end:
        if nums[i] <= nums[j]:
            # valid and not an inversion
            # add to output
            res.append(nums[i])
            # res.append(R[j])
            i += 1
        elif nums[i] > nums[j]:
            # inversion
            # everything after i is an inversion as its sorted
            count += mid - i
            res.append(nums[j])
            j += 1

    # One of the arrays could have elements remaining
    if i != mid:
        for k in range(i, mid):
            res.append(nums[k])
    elif j != end:
        for k in range(j, end):
            res.append(nums[k])

    # res is now sorted output
    nums[start:end] = res
    return count


input = [7, 12, 5, 4, 3, 1, 2, 8]
print(sortAndCount(input, 0, len(input)))
