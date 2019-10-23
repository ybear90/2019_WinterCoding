import heapq


def solution(stock, dates, supplies, k):
    heap = []
    root = (0, stock)
    heap.append(root)
    result = 0

    for dt, sup in zip(dates, supplies):
        node = (dt, sup)
        heapq.heappush(heap, node)
    print("heap: ", heap)

    while len(heap) > 1:
        head = heapq.heappop(heap)

        if head[1] > k - 1 - head[0]:
            break

        after_day = head[0] + 1
        after_stock = head[1] - 1
        new_head = (after_day, after_stock)

        if len(heap) == 1:
            # heap에 원소가 하나 남았을 때 마지막 공급이 필요한지 여부를 체크
            if new_head[1] < (k - 1) - new_head[0]:
                result += 1
                break
        print("after heap: ", heap)
        if new_head[0] < heap[0][0]:
            heapq.heappush(heap, new_head)
        # 공급 해야 하는 경우
        elif (new_head[0] == heap[0][0]) and (new_head[1] == 0):
            result += 1
        # 공급 이후 추가 공급이 필요한 경우
            if heap[0][1] < (k - 1) - heap[0][0]:
                continue
            else:
                break
        # 공급하지 않을 heap 요소를 패스하는 부분
        elif (new_head[0] == heap[0][0]) and (new_head[1] > 0):
            heapq.heappop(heap)
            heapq.heappush(heap, new_head)

    return result

print(solution(4, [4, 10, 15], [20, 5, 10], 30))
print(solution(10, [5, 10], [1, 100], 110))
print(solution(4, [1, 2, 3, 4], [10, 40, 20, 30], 100))

