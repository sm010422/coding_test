def solution(food):
    h_many = []
    result_list = []
    real_ = []

    for i in range(1, len(food)):
        h_many.append(food[i] // 2)

    for i in range(len(h_many)):
        for j in range(h_many[i]):
            result_list.append(i + 1)
            real_.append(i + 1)

    real_.reverse()
    result_list.append(0)

    for i in real_:
        result_list.append(i)

    answer = "".join(map(str, result_list))

    return answer
