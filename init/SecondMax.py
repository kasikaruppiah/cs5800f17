# Uses python3
import sys


def merge(a, l, m, r):
    b = a[l:m + 1]
    c = a[m + 1:r + 1]

    ai = l
    bi = 0
    ci = 0

    while (bi < len(b) and ci < len(c)):
        if (b[bi] < c[ci]):
            a[ai] = b[bi]
            bi += 1
        else:
            a[ai] = c[ci]
            ci += 1
        ai += 1

    while (bi < len(b)):
        a[ai] = b[bi]
        bi += 1
        ai += 1

    while (ci < len(c)):
        a[ai] = c[ci]
        ci += 1
        ai += 1


def mergeSort(a, l, r):
    if l < r:
        m = l + (r - l) // 2

        mergeSort(a, l, m)
        mergeSort(a, m + 1, r)

        merge(a, l, m, r)


def get_second_max(a, n):
    mergeSort(a, 0, n - 1)

    return a[-2]


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))

    print(get_second_max(a, n))