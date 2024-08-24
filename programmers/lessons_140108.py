def solution(s):
    first_letter = ""
    first_count = 0
    diff_count = 0
    result = 0

    for letter in s:
        if first_letter == "":
            first_letter = letter
            first_count += 1
            continue

        if letter == first_letter:
            first_count += 1
        else:
            diff_count += 1

        if first_count == diff_count:
            result += 1
            first_count = 0
            diff_count = 0
            first_letter = ""

    if first_letter:
        result += 1

    return result
