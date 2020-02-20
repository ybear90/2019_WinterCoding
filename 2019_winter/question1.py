"""
question1 : 직사각형 타일 내 사용하지 못하는 1x1 정사각형 갯수 구하기

백준 2168번 타일 위의 대각선 변형 문제(최대공약수 문제)

타일위에 대각선이 올라가게 되는 수학적인 규칙성을 찾았으면 되는 문제

특별한 알고리즘이 필요한 문제는 아니였다

참고 문제 : 백준 2168번

"""
# 유클리드 호제법을 이용한 최대공약수 구하기
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def solution(w, h):
    unused = w + h - gcd(w, h)
    return w * h - unused

print(solution(8, 12))
print(solution(3, 5))
print(solution(9, 9))