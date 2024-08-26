def solution(k, score):
    list_ = []
    result = []

    for i in range(len(score)):
        list_.append(score[i])
        list_.sort()
        list_.reverse()

        if i < k - 1:
            result.append(list_[i])
        else:
            result.append(list_[k - 1])

    answer = result
    return answer
