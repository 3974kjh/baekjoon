import sys

def pushheap(heap, l):
    while (l > 1):
        if (heap[l] > heap[l//2]):
            heap[l],heap[l//2] = heap[l//2],heap[l]
            l = l//2
        else:
            break

def maxheap(heap):
    l = len(heap) - 1
    maxnum = heap[1]
    out.append(maxnum)
    heap[1], heap[l] = heap[l], heap[1]
    heap.pop()
    idx = 2
    while (l - 1 > idx):
        if (l - 1) % 2 == 1 and heap[idx] < heap[idx + 1]:
            idx+=1
        if heap[idx] > heap[idx//2]:
            heap[idx],heap[idx//2] = heap[idx//2],heap[idx]
            idx = idx * 2
        else:
            break
    if l == 3 and heap[1] < heap[2]:
        heap[1],heap[2] = heap[2],heap[1]
    return (maxnum)

T = int(sys.stdin.readline())
heap = [0]
out = []
count = 0
for i in range(T):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 1:
            print(0)
        else:
            print(maxheap(heap))
    else:
        heap.append(num)
        pushheap(heap, len(heap) - 1)
print(out)