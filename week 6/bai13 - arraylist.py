def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for it in intervals:
        if not merged or merged[-1][1] < it[0]: merged.append(it)
        else: merged[-1][1] = max(merged[-1][1], it[1])
    return merged
print(merge_intervals([[1, 3], [2, 6], [8, 10]]))