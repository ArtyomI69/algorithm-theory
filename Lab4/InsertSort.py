def insertion_sort(alist):
    sortedList = alist.copy()
    for i in range(1, len(sortedList)):
        temp = sortedList[i]
        j = i - 1
        while j >= 0 and temp < sortedList[j]:
            sortedList[j + 1] = sortedList[j]
            j = j - 1
        sortedList[j + 1] = temp
    return sortedList
