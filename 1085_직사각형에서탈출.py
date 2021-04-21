x,y,w,h = map(int, input().split())
here = []
here.append(abs(x - w))
here.append(abs(y - h))
here.extend([x,y,w,h])
print(min(here))