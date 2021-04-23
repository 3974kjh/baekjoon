N = int(input())
people = []
for i in range(N):
    weight,length = map(int, input().split())
    people.append((weight, length))
for x,y in people:
    cnt = 1
    for a,b in people:
        if x < a and y < b:
            cnt+=1
    print(cnt,end=' ')
print('')