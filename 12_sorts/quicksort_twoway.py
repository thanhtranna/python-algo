import random


def QuickSort(arr):
    # Two-way sorting: improve the performance of non-random input
    # No extra space is needed, sorting inside the array to be sorted
    # The benchmark value is randomly selected by random
    # Input parameters: array to be sorted, array start index 0, array end index len(array)-1
    if arr is None or len(arr) < 1:
        return arr

    def swap(arr, low, upper):
        tmp = arr[low]
        arr[low] = arr[upper]
        arr[upper] = tmp
        return arr

    def QuickSort_TwoWay(arr, low, upper):
        # Small array sort i can use insert or select sort
        # if upper-low < 50: return arr
        # Baseline condition: low index = upper index; that is, the interval with only one value
        if low >= upper:
            return arr
        # Randomly select the reference value, and replace the reference value to the first element of the array
        swap(arr, low, int(random.uniform(low, upper)))
        temp = arr[low]
        # Cache boundary values, sort at the same time from the upper and lower boundaries
        i, j = low, upper
        while True:
            # The first element is the base value, so skip it
            i += 1
            # In the cell, sort
            # Starting from the lower boundary to find an index greater than the reference value
            while i <= upper and arr[i] <= temp:
                i += 1
            # Starting from the upper boundary to find an index smaller than the reference value
            # Because j must be greater than i, so the index value must be in the cell
            while arr[j] > temp:
                j -= 1
            # If the small index is greater than or equal to the large index, the sorting is complete and the sorting is exited
            if i >= j:
                break
            swap(arr, i, j)
        # Switch the index of the reference value from the lower boundary to the index split point
        swap(arr, low, j)
        QuickSort_TwoWay(arr, low, j - 1)
        QuickSort_TwoWay(arr, j + 1, upper)
        return arr

    return QuickSort_TwoWay(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    QuickSort(a1)
    print(a1)
    QuickSort(a2)
    print(a2)
    QuickSort(a3)
    print(a3)
    QuickSort(a4)
    print(a4)
