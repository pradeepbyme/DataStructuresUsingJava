def merge_sorted_array(a, b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    while i < len_a:
        sorted_list.append(a[i])
        i += 1

    while j < len_b:
        sorted_list.append(b[j])
        j += 1

    return sorted_list


a = [1, 3, 4, 5, 7, 13]
b = [2, 6, 8, 9, 13, 14]
print(merge_sorted_array(a, b))
