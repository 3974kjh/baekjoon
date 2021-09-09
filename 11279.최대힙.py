import sys

def pushheap(heap, l):
    while (l > 1):
        if (heap[l] > heap[l//2]):
            heap[l],heap[l//2] = heap[l//2],heap[l]
            l = l//2
        else:
            break

def maxheap(heap):
    maxnum = heap[1]
    heap[1], heap[len(heap)-1] = heap[len(heap)-1], heap[1]
    heap.pop()
    l = len(heap) - 1
    idx = 2
    while (l >= idx):
        if  l > idx and heap[idx] < heap[idx + 1]:
            idx+=1
        if heap[idx] > heap[idx//2]:
            heap[idx],heap[idx//2] = heap[idx//2],heap[idx]
            idx = idx * 2
        else:
            break
    return (maxnum)

T = int(sys.stdin.readline())
heap = [0]
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