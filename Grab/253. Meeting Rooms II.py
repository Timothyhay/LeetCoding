'''
    Others

    if encounter two consecutive start times that means we need two meeting rooms at that time.
    When we encounter an end time, it indicates we are done with a meeting and we don’t need that meeting room.

'''

def minMeetingRooms(intervals):
    starts = sorted(x[0] for x in intervals)
    ends = sorted(x[1] for x in intervals)
    sptr = 0
    eptr = 0
    ans = 1
    crt_cnt = 0
    while sptr < len(intervals):
        if starts[sptr] < ends[eptr]:
            sptr += 1
            crt_cnt += 1
        else:
            eptr += 1
            crt_cnt -= 1
        ans = max(ans, crt_cnt)
    return ans



print(minMeetingRooms([[9,10],[4,9],[5,17]]))
# Output: 2