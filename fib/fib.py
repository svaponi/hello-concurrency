def fib(n):
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    for index, expect in enumerate(expected):
        actual = fib(index)
        print(f"fib({index}): {actual}")
        assert actual == expect, f"fib({index}) failed: {expect=} {actual=}"
