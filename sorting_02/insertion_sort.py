def insertion_sort(a: list):
    for j in range(2, len(a)):
        key = a[j]
        # insert a[j] into sorted sequence A[1..j-1]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key


if __name__ == "__main__":
    a = [5, 2, 4, 6, 1, 3]
    print(a)
    insertion_sort(a)
    print(a)
