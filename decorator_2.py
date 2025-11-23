l = input()


def show_list(f):
    def wrapper(l):
        print(*sorted(f(l)))  #без return 
    return wrapper

@show_list
def get_list(l):
    return list(map(int, l.split()))


get_list(l) #без print(), иначе None
