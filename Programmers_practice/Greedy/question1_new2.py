def solution(n, lost, reserve):
    s = set(lost) & set(reserve)
    l = set(lost) - s # 빌릴 필요가 없는 학생을 제외
    r = set(reserve) - s # 여벌의 체육복을 가져왔으며 도난을 당하지 않은 학생의 집합

    for x in sorted(r):
        if x - 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x + 1)

    return n - len(l)