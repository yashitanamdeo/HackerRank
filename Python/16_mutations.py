# Approach 1 :
    #convert the string to a list and then change the value
def mutate_string(string, position, character):
    lst = list(string)
    lst[position] = character
    string = "".join(lst)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)