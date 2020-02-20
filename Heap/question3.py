"""
디스크 컨트롤러
"""

import heapq

def solution(jobs):
    last = -1
    now = 0
    used_time = 0
    task_wait = []
    task_count = 0

    while task_count < len(jobs):
        for job in jobs:
            if last < job[0] <= now:
                used_time += now - job[0]
                heapq.heappush(task_wait, job[1])
        if len(task_wait) > 0:
            used_time += len(task_wait) * task_wait[0]
            last = now
            now += heapq.heappop(task_wait)
            task_count += 1
        else:
            # 시간은 계속 1ms씩 흘러가므로
            now += 1

    return used_time // len(jobs)