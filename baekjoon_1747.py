input_number = int(input())


def is_fellinderom(i):
    compare = str(i)
    st_len = len(str(i))
    if st_len % 2 == 0:
        for j in range(st_len // 2):
            # print("even",j," ", compare[j])
            if compare[j] != compare[st_len-1 - j]:
                return False
        return True
    else:
        for k in range(st_len//2):
            # print("odd",k," ", compare[k])
            if compare[k] != compare[st_len-1 - k]:
                return False
        return True

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


#print(is_fellinderom(input_number))
# print("------------------------")

while (True):
    if is_prime(input_number):
        if is_fellinderom(input_number):
            break
    input_number += 1



# print(f"Answer is : {input_number}")
print(input_number)
