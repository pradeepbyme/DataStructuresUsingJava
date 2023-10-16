import bubble_sort as bs


def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


def quick_sort(elements, start, end):
    pivot_index = 0
    pivot = elements[pivot_index]
    start = pivot_index + 1
    end = len(elements) - 1

    while start < end and len(elements) > 1:
        if elements[start] < pivot:
            start += 1
        if elements[end] > pivot:
            end -= 1
        swap(start, end, elements)
    swap(pivot_index, end, elements)
    bs.bubble_sort(elements)
    # # elements[end], pivot = pivot, elements[end]
    # print(elements)
    # print("Start at element : ",elements[start], start)
    # print("End is at element : ",elements[end], end)
    # print(pivot)


# elements = [11, 9, 29, 7, 2, 15, 28]
# quick_sort(elements)

tests = [[11, 9, 29, 7, 2, 15, 28],
         [34, 12, 15, 11, 13],
         [3443, 434343, 1323]]
for elements in tests:
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)
