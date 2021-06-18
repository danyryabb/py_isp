class Intervals:
    def __init__(self, intervals):
        self.intervals = sorted(intervals, key=lambda i: i[0])

    def append(self, interval: tuple):
        new_interval_start, new_interval_end = interval[0], interval[1]
        for start, end in self.intervals:
            if end >= new_interval_start:
                new_interval_start = min(new_interval_start, start)
            if start <= new_interval_end:
                new_interval_end = max(new_interval_end, end)

        i = 0
        while i < len(self.intervals):
            start, end = self.intervals[i]
            if start >= new_interval_start and end <= new_interval_end:
                self.intervals.pop(i)
            else:
                i += 1

        self.intervals.append((new_interval_start, new_interval_end))
        self.__init__(self.intervals)


intervals = [(1, 3), (4, 5), (6, 7), (10, 23)]
inter = Intervals(intervals)
inter.append((2, 4))
print(intervals)
print(inter.intervals)
print()

intervals = [(1, 3), (4, 5), (6, 7), (10, 23)]
inter = Intervals(intervals)
inter.append((2, 7))
print(intervals)
print(inter.intervals)
print()

intervals = [(1, 3), (4, 5), (6, 7), (10, 23)]
inter = Intervals(intervals)
inter.append((5, 100))
print(intervals)
print(inter.intervals)
