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


"""
Given a string `s`, return the string with **all characters reversed**.

You must not use built-in reverse() or slicing shortcuts like s[::-1].

Constraints:
- Input: a single string
- Output: a reversed version of the string

Examples:
Input: "hello"
Output: "olleh"

Input: "Python is fun"
Output: "nuf si nohtyP"
"""

# solution 1
# def reverse_string(s):
#     words = s.strip().split(" ")
#     for idx, word in enumerate(words):
#         words[idx] = "".join(reversed(word))
#     return " ".join(reversed(words))


# solution 2 -> walking back
def reverse_string(s):
    result = ""
    for i in range(len(s) - 1, -1, -1):
        result += s[i]
    return result


@test_runner(
    expected=["olleh", "nuf si nohtyP", ""],
    assert_is_array=True,
    message="Reverse characters in a string",
)
def test_reverse_string(arr):
    return reverse_string(arr)


if __name__ == "__main__":
    # test_reverse_words(
    #     ["   Hello   world  ", "  I   love    we code   ", "   Kenya loves   AI   "]
    # )
    test_reverse_string(["hello", "Python is fun", ""])
