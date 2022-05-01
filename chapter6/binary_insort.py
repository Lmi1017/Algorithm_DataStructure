from typing import MutableSequence
import bisect


def binary_insertion_sort(a: MutableSequence) -> None:
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)
