if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))   #hash() is one of the functions in the __builtins__ module, so it need not be imported.