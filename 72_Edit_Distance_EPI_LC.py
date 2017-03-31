class Solution:

	def editDistance(self, word1, word2):

		cols = len(word1) + 1  # plus 1 for the null string column
		rows = len(word2) + 1 # plus 1 for the null string row

		dp = [[0] * cols for _ in range(rows)]

		# count = 0
		for c in range(cols):
			dp[0][c] = c  # setting the vals for the null row

		for r in range(rows):
			dp[r][0] = r # setting the vals for the null column


		# imagine the souce aligned along the cols and target along the rows
		for i in range(1, rows): # i corresponds to target
			for j in range(1, cols): # j corresponds to source
				if word2[i - 1] == word1[j - 1]:
					# characters match
					# take the diagonal value
					dp[i][j] = dp[i-1][j-1]
				else:
					# take min of north cells, north-west cell (i,e diagonal) and west cell and add 1 to it

					# min takes only 2 arguments
					dp[i][j] = 1 + min(min(dp[i-1][j], dp[i-1][j-1]), dp[i][j-1])

		return dp[rows -1][cols-1]



print(editDistance("abcdef", "azced"))