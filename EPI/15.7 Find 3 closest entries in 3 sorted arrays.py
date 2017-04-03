def find_three_closest(sorted_arrays):
    l1 = len(sorted_arrays[0])
    l2 = len(sorted_arrays[1])
    l3 = len(sorted_arrays[2])

    a1 = sorted_arrays[0]
    a2 = sorted_arrays[1]
    a3 = sorted_arrays[2]

    i = j = k = 0

    min_distance = float('inf')
    min_three = []
    while i < l1 and j < l2 and k < l3:
        smallest = min(min(a1[i], a2[j]), a3[k])
        maximum = max(max(a1[i], a2[j]), a3[k])
        diff = maximum - smallest

        if diff < min_distance:
            min_distance = diff
            min_three = [a1[i], a2[j], a3[k]]

            if min_distance == 0:
                return min_three

        # move the pointer thats at the min element forward

        if smallest == a1[i]:
            i += 1
        elif smallest == a2[j]:
            j += 1
        else:
            k += 1

    return min_three


sorted_arrays = [
    [5, 10, 15],
    [3, 6, 9, 12, 15],
    [4, 15]
]
print(find_three_closest(sorted_arrays))
