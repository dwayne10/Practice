def  allPermutationsOfString(word, l, r, res):
    if l == r:
        res.append(''.join(word))
    for i in range(l, r+1):
        word[i], word[l] = word[l], word[i]
        allPermutationsOfString(word, l + 1, r, res)
        word[i], word[l] = word[l], word[i]
    return res

res= []
print(allPermutationsOfString(list("AAB"), 0, 2, res))
