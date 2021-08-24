def swap_case(s):
    ans = ""
    for letter in s:
        if letter == letter.upper():
            ans += letter.lower()
        else:
            ans += letter.upper()
    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)