# coding=utf-8

def fib(num):
    result = []
    a, b = 0, 1

    while num > 0:
        result.append(a)
        a, b = b, a + b
        num = num - 1

    print(result)


if __name__ == "__main__":
    fib(15)
