
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort(key=lambda x:x[0])
n = len(intervals)
for i in range(n):
    for j in range(i, n):
        if intervals[i][0] > intervals[j][0]:
            temp = intervals[i]
            intervals[i] = intervals[j]
            intervals[j] = temp
termenal = []
for y in range(n):
    if not termenal or termenal[-1][1] < intervals[y][0]:
        termenal.append(intervals[y])
    else:
        termenal[-1][1] = max(termenal[-1][1], intervals[y][1])

print(df)