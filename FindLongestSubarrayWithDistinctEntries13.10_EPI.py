def longestSubarray(arr):

    seq = []
    length_so_far = max_length = 0
    index_map = {}
    for index, char in enumerate(arr):
        if char not in index_map:
            # seq.append(char)
            index_map[char] = index
            length_so_far += 1
        else:
            max_length = max(length_so_far, max_length)
            length_so_far = index - index_map[char]
            index_map[char] = index
    return max(max_length, length_so_far)

input = 'sqlsqlvarun'
print(longestSubarray(list(input)))