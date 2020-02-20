"""
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때
소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항

nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

"""
import math

def is_prime(num):
    if num % 2 == 0 or num == 1:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def solution(nums):
    # pick possible list
    answer = 0
    possible_list = []
    prime_list = []

    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                sub_list = []
                sub_list.append(nums[i])
                sub_list.append(nums[j])
                sub_list.append(nums[k])
                possible_list.append(sub_list)

    sum_list = [sum(x) for x in possible_list]
    # duplicate delete
    # sum_list = list(set(sum_list))
    print("sum_list: ", sum_list)

    for val in sum_list:
        if is_prime(val):
            answer += 1

    return answer