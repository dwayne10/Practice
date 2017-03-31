def recursiveAdd(list):
	if len(list) == 1:
		return list[0]
	return list[0] + recursiveAdd(list[1:])










	def recursive_reverse_str(sent):
		if len(sent) <= 1:
			return sent
		else:
			return recursive_reverse_str(sent[1:]) + sent[0]