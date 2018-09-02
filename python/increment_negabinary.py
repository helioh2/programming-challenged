

def encode(n):  # Converts from decimal
    if n == 0:
        return [0]
    out = []
    while n != 0:
        n, rem = divmod(n, -2)
        if rem < 0:
            n += 1
            rem -= -2
        out.append(rem)
    return out




def decode(nstr):  # Converts to decimal
    if nstr == 0:
        return 0

    total = 0
    for i, ch in enumerate(nstr[::-1]):
        total += int(ch) * (-2) ** i
    return total

def solution(A):
    A.reverse()
    int_A = decode(A)
    int_A += 1
    res_string = encode(int_A)
    return res_string


print(solution([1,0,1]))
