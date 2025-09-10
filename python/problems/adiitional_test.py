def printnNumbers(target, n=0):
    if n == target:
        return
    if n % 2 == 0:
        print(n)

    printnNumbers(target, n+1)


def reverseS(s):
    answer = ""
    def res(val, index, path):
        if index == len(s):
            answer = "".join(path)

        path.append(val)
        res(s[index], index+1, path)

    res(s[-1], 1, [s[-1]])
    print(answer)
    return answer




if __name__ == "__main__":
    printnNumbers(5)
    print(reverseS("Shad"))
