import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    # 조건이 길어서 무한 루프를 걸고 특정조건에서 break 걸게끔 설게
    while True:
        min1 = heapq.heappop(scoville)
        # 탈출 조건 설계
        if min1 >= K:
            break
        elif len(scoville) == 0:
            answer = -1
            break
        min2 = heapq.heappop(scoville)
        new_scoville = min1 + 2 * min2
        heapq.heappush(scoville, new_scoville)
        answer += 1

    return answer