def solution(s):
    # 스택을 사용하여 풀이
    # push, pop 연산을 사용하기 위해
    list_s = list(s)
    stack = []

    for ch in list_s:
        stack.append(ch)
        if len(stack) >= 2 and (stack[-1] == stack[-2]):
            stack.pop()
            stack.pop()

    if len(stack) == 0:
        return 1
    else:
        return 0