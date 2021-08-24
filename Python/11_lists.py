if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        string = input().split()
        cmd = string[0]
        if cmd == "insert":
            lst.insert(int(string[1]), int(string[2]))
        elif cmd == "remove":
            lst.remove(int(string[1]))
        elif cmd == "append":
            lst.append(int(string[1]))
        elif cmd == "sort":
            lst.sort()
        elif cmd == "pop":
            lst.pop()
        elif cmd == "reverse":
            lst.reverse()
        else:
            print(lst)  