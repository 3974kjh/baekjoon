N = list(map(str, input()))
check = [[],[],['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
cnt = 0
here = 0
for i in N:
    for j in range(len(check)):
        if i in check[j]:
            here = j + 1
            cnt+=here
print(cnt)
