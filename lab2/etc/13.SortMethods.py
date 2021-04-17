def partition(nums, low, high):  
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):  
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)


def merge(left_list, right_list):  
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list


def merge_sort(nums):  
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)


def radixSort(arr):
    rang = 10
    maxLen = len(str(max(arr)))
    for step in range(maxLen):
        arrays = [[] for i in range(rang)]
        for element in arr:
            arrays[int(((element % int(rang**(step+1))) / int(rang**step)))].append(element)
        arr = []
        for section in arrays:
            arr.extend(section)
    return arr

list_of_nums_fst = [22, 5, 1, 18, 99]  
quick_sort(list_of_nums_fst)  
print(list_of_nums_fst)

list_of_nums_sec = [120, 45, 68, 250, 176]  
list_of_nums_sec = merge_sort(list_of_nums_sec)  
print(list_of_nums_sec)

list_of_nums_th = [12, 5, 664, 63, 5, 73, 93, 127, 432, 64, 34]
list_of_nums_th = radixSort(list_of_nums_th)
print(list_of_nums_th)




