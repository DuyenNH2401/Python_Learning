import random
def heapify(arr, last):
    for i in range(last, 0, -1):
        root = (i-1)//2
        if arr[root] < arr[i]:
            arr[i], arr[root] = arr[root], arr[i]
    arr[0], arr[last] = arr[last], arr[0]

    if last > 2:
        return heapify(arr, last-1)
    else: return arr

def heap_sort(arr):
    last = len(arr) - 1
    print(heapify(arr, last))

def main():
    list = random.sample(range(1,101),100)
    heap_sort(list)

if __name__ == "__main__":
    main()