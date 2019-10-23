def solution(heights):
    answer = [0] * len(heights)
    current_index = len(heights) - 1
    while len(heights) > 0:
        current_tower = heights.pop()
        # print("current_tower: ", current_tower, "current_index: ", current_index)
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > current_tower:
                # print("current height: ", heights[i])
                answer[current_index] = i + 1
                # print("current answer: ", answer)
                break
        current_index -= 1

    print("final answer: ", answer)

    return answer