# Счетчик через замыкания

def counter_add(N):
    def plus1():
        nonlocal N 
        N += 1
        return N

    return plus1


cnt = counter_add(10)
print(cnt()) # 11
print(cnt()) # 12
print(cnt()) # 13
