def find_max_sim_events(events):

    if not events or len(events) == 1:
        return 0
    max_sim = 1
    curr_sim = 1

    # sort by start times
    events.sort(key=lambda x: x[0])

    # list of concurrent parts
    res = []
    res.append(events[0])

    for event in events[1:]:
        s1, e1 = res[-1]
        s2, e2 = event[0], event[1]

        if e1 > s2:
            # they are concurrent
            curr_sim += 1
            res[-1] = [max(s1, s2), min(e1, e2)]
        else:
            # not concurrent
            max_sim = max(max_sim, curr_sim)
            curr_sim = 1
            res.append(event)

    return max_sim if max_sim != 1 else 0

events = [[2,7], [1,2], [9,10], [4,15]]
print(find_max_sim_events(events))
