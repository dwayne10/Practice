def numberOfCombination(target, scores):
    scores.sort()

    # create matrix of number of rows = number of scores
    # and the number of columns == target

    dp_table = [[0]*(target+1) for _ in range(len(scores))]

    for score in range(len(scores)):
        dp_table[score][0] = 1
        for t in range(1, target+1):
             # only one way to get to 0

            # have option of using this score or not using it
            with_score =  dp_table[score][t - scores[score]] if t >= scores[score] else 0

            without_score = dp_table[score-1][t] if score >= 1 else 0

            dp_table[score][t] = with_score + without_score

    return dp_table[len(scores) -1][target]


print(numberOfCombination(12, [2,3,7]))
