if __name__ == '__main__':
    i = int(input())
    lis = list(map(int,input().split()))
    z = max(lis)
    while max(lis) == z:
        lis.remove(max(lis))

    print (max(lis))



# if __name__ == '__main__':
#     n = input()
#     arr = list(map(int, input().split()))
#     if len(arr) > 2:
#         mx = max(arr[0],arr[1])
#         secondmx = min(arr[0],arr[1])
#         for i in range(2,len(arr)):
#             if arr[i] > mx:
#                 secondmx = mx
#                 mx = arr[i]
#             elif arr[i] > secondmx and mx != arr[i]:
#                 secondmx = arr[i]
#         print(secondmx)
#     else:
#         arr.sort()
#         newarr = set(arr)
        
#         while max(newarr) == mx:
#             mx = max(arr)
#             newarr.remove(max(newarr))
            
#         print(max(arr))
                