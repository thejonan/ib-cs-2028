def sort_numbers(a: list[any]):  # type: ignore
    """Sorts the provided array of number in ascending order.

    Args:
        a (list[any]): The array to be sorted in-place.
    """
    pass

# DON'T EDIT BELOW THIS LINE


# Test 1: Unsorted array
a = [5, 2, 8, 1, 3]
sort_numbers(a)
assert a == [1, 2, 3, 5, 8]

# Test 2: Already sorted array
a = [1, 2, 3, 4, 5]
sort_numbers(a)
assert a == [1, 2, 3, 4, 5]

# Test 3: Array sorted in descending order
a = [5, 4, 3, 2, 1]
sort_numbers(a)
assert a == [1, 2, 3, 4, 5]

# Test 4: Array containing duplicate values
a = [3, 1, 3, 2, 1, 2]
sort_numbers(a)
assert a == [1, 1, 2, 2, 3, 3]

# Test 5: Negative and fractional numbers
a = [2.5, -3, 0, -1.5, 4, 0.5]
sort_numbers(a)
assert a == [-3, -1.5, 0, 0.5, 2.5, 4]

# Test 6: Array containing a single element
a = [42]
sort_numbers(a)
assert a == [42]

# Test 7: Empty array
a = []
sort_numbers(a)
assert a == []

# Test 8: Array containing identical values
a = [7, 7, 7, 7]
sort_numbers(a)
assert a == [7, 7, 7, 7]

print("All tests passed!")
