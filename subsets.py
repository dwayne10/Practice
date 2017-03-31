def subsets(end):
    def is_a_solution(a, start, end):
        return start == end

    def process_solution(a, start):
        print("{")
        for i in range(start):
            if a[i] is True:
                print(i)
        print("}")

    def construct_candidates(a, start, end):
        a[start] = True
        a[end] = False
        return 2

    def backtrack(a, start, end):

        if is_a_solution(a, start, end):
            process_solution(a, start)
        else:
            start = start + 1
            ncandidates = construct_candidates(a, start, end)
            for i in range(ncandidates):
                # a[start] = c[i]
                backtrack(a, start, end)

    a = [None] * end

    backtrack(a, 0, end - 1)


print(subsets(5))
