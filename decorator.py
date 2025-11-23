import time


def test_time(fn):
    def wrapper(*args, **kwargs):
        st = time.time() # что-то делаем до функции
        res = fn(*args, **kwargs)
        dt = time.time() - st # что-то делаем после функции
        print(f"Время работы: {dt} сек")
        return res

    return wrapper

@test_time
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b

    return a

# get_fast_nod = test_time(get_fast_nod) альтернатива
print(get_fast_nod(1, 2))
