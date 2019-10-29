import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    trial = 0

    # length == 1 case processing
    if len(scoville) == 1:
        if scoville[0] < K:
            return -1
        else:
            return trial

    # find scov trial
    while scoville[0] < K and len(scoville) > 1:
        best_min = heapq.heappop(scoville)
        second_min = heapq.heappop(scoville)

        mix_scov = best_min + (2 * second_min)

        heapq.heappush(scoville, mix_scov)

        trial += 1

    if max(scoville) < K:
        return -1

    return trial

print(solution([1, 2, 3, 9, 10, 12], 7))