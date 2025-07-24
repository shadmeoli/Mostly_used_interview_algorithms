"""
Given a string, reverse the order of words.
Words are separated by one or more spaces.
You must remove leading/trailing spaces and reduce multiple spaces to a single space.

Example:
Input: "   Hello   world  "
Output: "world Hello"
"""

from python.tester.testLogger import test_runner

reverse_words = lambda s: " ".join(
    reversed([word for word in s.strip().split(" ") if word])
)


@test_runner(
    expected=[
        "world Hello",
        "code we love I",
        "AI loves Kenya",
    ],
    assert_is_array=True,
    message="Reverse words in a string",
)
def test_reverse_words(arr):
    return reverse_words(arr)


if __name__ == "__main__":
    test_reverse_words(
        ["   Hello   world  ", "  I   love    we code   ", "   Kenya loves   AI   "]
    )
