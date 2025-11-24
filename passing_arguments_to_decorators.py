from functools import wraps


def decorator_func(start=0):
    def get_func(func):
        @wraps(func)       # Позволяет оставить прежними описание и имя декорируемой функции
        def wrapper(s):
            res = func(s)
            return res + start
          
        # wrapper.__name__ = func.__name__
        # wrapper.__doc__ = func.__doc__
        
        return wrapper

    return get_func


@decorator_func(start=5)
def sum_lst(s):
    """Функция нахождения суммы значений списка"""
    lst = [int(i) for i in s.split()]
    return sum(lst)


n = input() # 5 6 3 6 -4 6 -1
print(sum_lst.__name__, sum_lst.__doc__) # sum_lst Функция нахождения суммы значений списка
print(sum_lst(n)) # 26
