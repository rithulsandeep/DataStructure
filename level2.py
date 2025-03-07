class IntervalMerger:
    def __init__(self):
        self.intervals = []

    def addInterval(self, start, end):
        self.intervals.append([start, end])
        self.intervals.sort()
        merged = []
        for interval in self.intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        self.intervals = merged

    def getIntervals(self):
        return self.intervals