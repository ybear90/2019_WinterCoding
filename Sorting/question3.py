"""
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다.

위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h가 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때,

이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

* 제한사항
1. 과학자가 발표한 논문의 수는 1편 이상 1000편 이하입니다.
2. 논문별 인용 횟수는 0회 이상 10000회 이하입니다.
"""
def solution(citations):
    # h-index를 헷갈리지 않게 계산하기 위해선 내림차순으로 정렬해 주는 것이 유리
    # 오름차순 그대로 할 경우 올바른 h-index를 구할 때 까지 작은 h-index 후보군을 필히 탐색하게 되므로 불필요한 연산이 생김
    citations.sort(reverse=True)
    # n = len(citations)
    h_index = 0

    for idx, rep in enumerate(citations):
        # print("idx: ", idx, "rep: ", rep)
        if rep <= idx:
            h_index = idx
            break
        # if min(citations) > len(citations):
        #     h_index = len(citations)
        #     break
        # if len(citations[:idx]) <= rep and rep <= len(citations[idx:]):
        #     h_index = rep
    if min(citations) > len(citations):
        h_index = len(citations)

    return h_index


print(solution([3, 0, 6, 1, 5])) # 3
print(solution([0, 0, 0, 0, 0])) # 0
print(solution([0, 1, 1, 1, 1])) # 1
print(solution([2, 7, 5])) # 2
print(solution([3, 4, 5, 6])) # 3
print(solution([4, 5, 6])) # 3
print(solution([22, 42])) # 2
print(solution([20, 19, 18, 1])) # 3
