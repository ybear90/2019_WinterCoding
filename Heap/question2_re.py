import heapq


def solution(stock, dates, supplies, k):
    heap = []
    result = 0
    date_start = 0

    while stock < k:
        for i in range(date_start, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(heap, (-supplies[i], supplies[i]))
                date_start += 1
            else:
                break
        stock += heapq.heappop(heap)[1]
        result += 1

    return result