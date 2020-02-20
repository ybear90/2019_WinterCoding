"""
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,

어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록

solution 함수를 작성해주세요.

* 제한 사항
1. phone_book의 길이는 1 이상, 1000000 이하입니다.
2. 각 전화번호의 길이는 1 이상 20 이하입니다.
"""
def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: len(x))

    for idx, number in enumerate(phone_book):
        hhash = {}
        hhash[number] = hhash.get(number, 0) + 1

        if idx < len(phone_book) - 1:
            for number2 in phone_book[idx+1:]:
                # 기준이 되는 접두어 number와 number2[:len(number)]가 같지 않은 sub접두어면 중복해서 접두어 갯수를 늘리지 않는다
                # (예외처리를 위함 : ["111113", "1112", "12"])
                if hhash.get(number2[:len(number)], 0) == 1 and number != number2[:len(number)]:
                    continue
                hhash[number2[:len(number)]] = hhash.get(number2[:len(number)], 0) + 1
        print("current hash: ", hhash)
        for _, value in hhash.items():
            if value != 1:
                answer = False
                break

        if answer == False:
            break

    return answer





print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
print(solution(["111113", "1112", "12"]))