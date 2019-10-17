def solution(participant, completion):
    participant.sort() # O(nlgn)
    completion.sort() # O(nlgn)

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[len(participant)-1]