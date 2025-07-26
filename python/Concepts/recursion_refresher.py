from python.tester.testLogger import test_runner


def recursiveBubbleSort(arr, n=None, ind=0):
    if n is None:
        n = len(arr)

    if n == 1:
        return arr

    if ind == n - 1:
        return recursiveBubbleSort(arr, n - 1, 0)

    if arr[ind] > arr[ind + 1]:
        arr[ind], arr[ind + 1] = arr[ind + 1], arr[ind]
    return recursiveBubbleSort(arr, n, ind + 1)


@test_runner(
    expected=[[2, 4, 6, 8]], assert_is_array=True, message="Bubble sort with recursion"
)
def test_recursive_bubble_sort(arr):
    return recursiveBubbleSort(arr)


def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


@test_runner(
    expected="edoc", assert_is_array=False, message="Bubble sort with recursion"
)
def test_recursive_reverse_string(arr):
    return reverse_string(arr)


if __name__ == "__main__":
    # test_recursive_bubble_sort([[2, 8, 6, 4]])
    test_recursive_reverse_string("code")
