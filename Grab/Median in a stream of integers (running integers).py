'''
    Heap

    we can use a max heap on the left side to represent elements that are less than effective median,
    and a min-heap on the right side to represent elements that are greater than effective median.
    After processing an incoming element, the number of elements in heaps differs utmost by 1 element.
    When both heaps contain the same number of elements, we pick the average of heaps root data as effective median.
    When the heaps are not balanced, we select effective median from the root of the heap containing more elements.

    Time Complexity: If we omit the way how stream was read, complexity of median finding is O(N log N),
    as we need to read the stream, and due to heap insertions/deletions.
    Auxiliary Space: O(N)

    if we use nsertion sort takes O(n^2) time to sort n elements.
    Perhaps we can use binary search on insertion sort to find the location of the next element in O(log n) time.
    Yet, we can’t do data movement in O(log n) time. No matter how efficient the implementation is,
    it takes polynomial time in case of insertion sort.
'''

from heapq import heappush, heappop, heapify
import math

minHeap = []
heapify(minHeap)
maxHeap = []
heapify(maxHeap)


def insertHeaps(num):
    heappush(maxHeap, -num)  ### Pushing negative element to obtain a minHeap for
    heappush(minHeap, -heappop(maxHeap))  ### the negative counterpart

    if len(minHeap) > len(maxHeap):
        heappush(maxHeap, -heappop(minHeap))


def getMedian():
    if len(minHeap) != len(maxHeap):
        # maxHeap is negative
        return -maxHeap[0]
    else:
        # maxHeap is negative so minus too
        return (minHeap[0] - maxHeap[0]) / 2


if __name__ == '__main__':
    A = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
    n = len(A)
    for i in range(n):
        insertHeaps(A[i])
        print(math.floor(getMedian()))