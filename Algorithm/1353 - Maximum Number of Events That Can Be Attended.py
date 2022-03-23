class Solution:

    def maxEvents(self, events: List[List[int]]) -> int:
        
        class Event(object):
            def __init__(self, date):
                self.date = date
            def __lt__(self, other):
                if self.date[1] == other.date[1]:
                    return self.date[0] < other.date[0]
                else:
                    return self.date[1] < other.date[1]
        events.sort(reverse=False)  
        day = events[0][0]
        finday = events[-1][1]
        evptr = 0
        attend = 0
        from queue import PriorityQueue
        pq = PriorityQueue()
        while evptr < len(events) or not pq.empty():
            if pq.empty():
                day = events[evptr][0]
            while not pq.empty() and pq.queue[0].date[1] < day:
                pq.get()
            # print(evptr, pq.queue, day)
            while evptr < len(events) and events[evptr][0] <= day and events[evptr][1] >= day:
                pq.put(Event(events[evptr]))
                evptr += 1

            if not pq.empty() and pq.queue[0].date[1] >= day:
                a = pq.get()
                # print("attend", a)
                attend += 1

            day += 1

        return attend

'''
    def maxEvents(self, A):
        A.sort(reverse=1)
        h = []
        res = d = 0
        while A or h:
            if not h: d = A[-1][0]
            while A and A[-1][0] <= d:
                heapq.heappush(h, A.pop()[1])
            heapq.heappop(h)
            res += 1
            d += 1
            while h and h[0] < d:
                heapq.heappop(h)
        return res
'''