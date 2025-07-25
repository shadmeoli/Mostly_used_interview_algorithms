from python.tester.testLogger import test_runner


def recursiveBubbleSort(arr):
    pass


@test_runner(
    expected=[[2, 4, 6, 8]], assert_is_array=True, message="Bubble sort with recursion"
)
def test_recursive_bubble_sort(arr):
    return recursiveBubbleSort(arr)


if __name__ == "__main__":
    test_recursive_bubble_sort([[2, 8, 6, 4]])
