import textwrap

# without textwrap
def wrap(string, max_width):
    for i in range(0,len(string),max_width):
        result = string[i:i+max_width]
        if len(result) == max_width:
            print(result)
        else:
            return result

# with textwrap
def wrap(string, max_width):
    wrappedText = " ".join(textwrap.wrap(string,max_width))
    return(textwrap.fill(wrappedText,max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)