def solution(k, m, score):
    answer = 0

    list_ = list(score)

    list_.sort()
    list_.reverse()

    for j in range(1, len(score) // m + 1):
        answer += m * (list_[j * m - 1])

    return answer
