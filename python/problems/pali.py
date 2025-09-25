def longestPalindrome(s: str) -> str:
    pal = ""
    longest = ""
    for i in range(len(s)):
        for l, r in ((i, i), (i, i + 1)):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(longest):
                    longest = s[l : r + 1]
                    l -= 1
                    r += 1
    return longest


if __name__ == "__main__":
    # s = "babad"
    s = "cbbd"
    print(longestPalindrome(s))
