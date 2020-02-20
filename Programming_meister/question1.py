def solution(nums):
    # half_n = int(len(nums) / 2)
    # # possible_set = set()
    # possible_hash = {}
    # num_kind = -1
    # 아래의 pick 방법은 생각해보니 몇몇 경우의 수가 빠진다
    # 띄엄 띄엄 원소를 고르는 경우가 빠짐
    # for i in range(half_n):
    #     for j in range(half_n+i, len(nums)):
    #         make_list = nums[i:half_n + i - 1]
    #         make_list.append(nums[j])
    #         make_tuple = tuple(set(make_list))
    #         possible_hash[make_tuple] = possible_hash.get(make_tuple, 0) + 1
    # # print("possible_hash: ", possible_hash)
    # for kind in possible_hash.keys():
    #     num_kind = max(num_kind, len(kind))
    #
    # return num_kind
    half_n = int(len(nums) / 2)

    # duplicate remove
    nums = list(set(nums))
    print("after nums: ", nums)

    if len(nums) <= half_n:
        return len(nums)
    else:
        return half_n

print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))