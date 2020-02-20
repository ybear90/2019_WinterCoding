def solution(N, number):
    # 해집합의 리스트 초기화
    # 최솟값은 8을 넘어갈 수 없으므로 8개의 해집합을 구성
    sol_list = [set() for x in range(8)]
    # answer의 초깃값 설정
    answer = -1  # 아직 못찾은 상태

    # 해집합의 원소 초기화
    # enumerate start = 1 -> i 값을 0이 아닌 1무터 진행시킴
    for i, x in enumerate(sol_list, start=1):
        # i개수만큼의 수는 무조건 가지고 있으므로 해당 수를 미리 더해서 초기화
        x.add(int(str(N) * i))
        # 부분 해 집합을 모두 연산하여 전체 해 집합을 구하는 방법
        # 숫자가 한개인 부분 해집합부터 차례대로 올려가며 구함

    for i in range(1, len(sol_list)):
        for j in range(i):
            for elem1 in sol_list[j]:
                for elem2 in sol_list[i - j - 1]:
                    sol_list[i].add(elem1 + elem2)
                    sol_list[i].add(elem1 - elem2)
                    sol_list[i].add(elem1 * elem2)
                    if elem2 != 0:
                        sol_list[i].add(elem1 / elem2)
        if number in sol_list[i]:
            answer = i + 1
            break

    return answer

print(solution(5, 12))
print(solution(2, 11))