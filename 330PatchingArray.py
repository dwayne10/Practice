def minPatch(array, n):
	added = 0
	i = 0 
	miss = 1
	while miss <=n :
		if i <= len(array) and nums[i] <= miss:
			miss =  miss + nums[i]
			i += 1
		else:
			print("found missing number")
			print("miss before: ", miss)
			miss = miss + miss 
			print("miss after: ", miss)
			added += 1
	return added