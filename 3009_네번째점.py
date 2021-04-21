here = []
for i in range(3):
    x = map(int, input().split())
    here.extend(x)
ax=[]
ay=[]
for i in range(len(here)):
    if i == 0 or i == 2 or i == 4:
        ax.append(here[i])
    else:
        ay.append(here[i])
ax.sort()
ay.sort()
for i in range(2):
    if ax[i] == ax[i+1]:
        del(ax[i])
        del(ax[i])
        break
for i in range(2):
    if ay[i] == ay[i+1]:
        del(ay[i])
        del(ay[i])
        break
print(ax[0], ay[0])