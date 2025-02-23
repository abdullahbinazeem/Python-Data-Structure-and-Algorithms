def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]

#Using Hoare Partition Algorithm
def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]


    while start < end:
        while (elements[start] <= pivot) and start < end:
            start += 1

        while (elements[end] > pivot):
            end -= 1

        if start < end:
            swap(start, end, elements)
    
    swap(pivot_index, end, elements)
    return end

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)
        quick_sort(elements, pi+1, end)

if __name__ == '__main__':
    elements = [11, 0, 29, 7, 2, 15, 28]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)