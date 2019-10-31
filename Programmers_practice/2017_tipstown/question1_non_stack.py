def solution(s):
    idx = 0
    while idx < len(s) - 1:
        # print("current length: ", len(s), "current index: ", idx)
        if s[idx] == s[idx + 1]:
            # 맨 앞에서 제거되는 경우
            if idx == 0:
                s = s[idx + 2:]
            # 가운데서 제거되는 경우
            elif 0 < idx < len(s) - 2:
                s = s[:idx] + s[idx + 2:]
                idx -= 1
            # 뒤에서 제거되는 경우
            else:
                s = s[:idx]
                idx += 1
        else:
            idx += 1

    if len(s) == 0:
        answer = 1
    else:
        answer = 0

    return answer