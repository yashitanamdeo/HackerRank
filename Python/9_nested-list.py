if __name__ == '__main__':
    l = []
    second_lowest_names = []
    scores = set()

    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])
        scores.add(score)
            
    second_lowest = sorted(scores)[1]

    for name, score in l:
        if score == second_lowest:
            second_lowest_names.append(name)

    for name in sorted(second_lowest_names):
        print(name, end='\n')



# if __name__ == '__main__':
#     d={} 
#     for _ in range(int(input())):
#         Name = input() 
#         Grade = float(input())
#         d[Name]=Grade 
#     v=d.values()
#     second=sorted(list(set(v)))[1]
#     second_lowest=[] 
#     for key,value in d.items():
#         if value==second: 
#             second_lowest.append(key) 
#     second_lowest.sort() 
#     for name in second_lowest:
#         print(name) 