def solution(number, limit, power):
    answer = 0

    for i in range(1, number + 1):
        count = 0
        count_plus = 0

        for j in range(1, i + 1):
            if pow(j, 2) > i:
                break
            if pow(j, 2) == i:
                count_plus = 1
                break
            if (i) % (j) == 0:
                count += 2

        if count + count_plus > limit:
            answer += power
        else:
            answer += count + count_plus

    return answer
