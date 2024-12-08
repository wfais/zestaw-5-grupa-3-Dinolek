from ZADANIE1.tablica import MonitorowanaTablica

def insertion_sort(array: MonitorowanaTablica, left=0, right=None):
    if right is None:
        right = len(array) - 1

    i = left + 1
    while i <= right:
        j = i
        while j > left and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
        i += 1


def bubble_sort(array: MonitorowanaTablica):
    n = len(array)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                swapped = True

        if not swapped:
            break


def shell_sort(array: MonitorowanaTablica):
    left = 0
    right = len(array) - 1

    h = 1
    while h <= (right - left) // 9:
        h = 3 * h + 1

    while h > 0:
        for i in range(left + h, right + 1):
            j = i

            item = array[i]
            while j >= left + h and item < array[j - h]:
                array[j] = array[j - h]
                j = j - h
            array[j] = item

        h = h // 3




def merge_sort(array: MonitorowanaTablica, left=None, right=None):
# twoj kod
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1
    if left >= right:
        return

    middle = (left + right) // 2

    merge_sort(array, left, middle)
    merge_sort(array, middle + 1, right)

    merge(array, left, middle, right)


def merge(array: MonitorowanaTablica, left, middle, right):
    """Merges two sorted subarrays."""
    # twoj kod, moze sie przydac
    i, j = left, middle + 1
    merged = []

    while i <= middle and j <= right:
        if array[i] <= array[j]:
            merged.append(array[i])
            i += 1
        else:
            merged.append(array[j])
            j += 1

    while i <= middle:
        merged.append(array[i])
        i += 1

    while j <= right:
        merged.append(array[j])
        j += 1

    for idx, val in enumerate(merged):
        array[left + idx] = val


def quick_sort(array: MonitorowanaTablica, left=None, right=None):
    """Performs quick sort on the given array."""
    # twoj kod
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1
    if left >= right:
        return

    pivot = partition(array, left, right)
    quick_sort(array, left, pivot - 1)
    quick_sort(array, pivot + 1, right)


def partition(array: MonitorowanaTablica, left, right):
    """Partitions the array into two parts."""
    # twoj kod, moze sie przydac
    pivot = array[right]
    i = left

    for j in range(left, right):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[i], array[right] = array[right], array[i]
    return i


def tim_sort(array: MonitorowanaTablica):
# twoj kod
    n = len(array)
    run = 32

    for i in range(0, n, run):
        insertion_sort(array, i, min(i + run - 1, n - 1))

    size = run
    while size < n:
        for left in range(0, n, size * 2):
            merge(array, left, left + size - 1, min(left + size * 2 - 1, n - 1))

        size *= 2


algorytmy = [
    (insertion_sort, "Insertion Sort"),
    (bubble_sort, "Bubble Sort"),
    (shell_sort, "Shell Sort"),
    (merge_sort, "Merge Sort"),
    (quick_sort, "Quick Sort"),
    (tim_sort, "Tim Sort"),
]