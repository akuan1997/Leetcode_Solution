def meetingrooms(intervals):
    # intervals.sort() # method 1
    intervals.sort(key=lambda x: x[0])  # method 2

    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False
    return True