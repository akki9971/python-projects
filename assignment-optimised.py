def make_lists_equal(a, b):
    if isinstance(a, list) and isinstance(b, list):
        max_len = max(len(a), len(b))
        a = a + [0] * (max_len - len(a))
        b = b + [0] * (max_len - len(b))
        return a, b
    elif isinstance(a, list):
        return a, [b] + [0] * (len(a) - 1)
    elif isinstance(b, list):
        return [a] + [0] * (len(b) - 1), b
    else:
        return [a], [b]


def add_nested_lists(a, b):
    a, b = make_lists_equal(a, b)
    result = []

    for x, y in zip(a, b):
        if isinstance(x, list) or isinstance(y, list):
            result.append(add_nested_lists(x, y))
        else:
            result.append(x + y)

    return result


# Example test cases:
# A = [5, 0, 10, 6]
# B = [1, 2, 4]

# A = [5, 0, 10, [1, 1]]
# B = [1, 2, [0, 1]]

# A = [5, 0, [2,1], [1, 1, [4, 5, [55, 44]]]]
# B = [1, 2, [0, 1]]

A = [5, 0, [2,1], [1, 1, [4, 5, [55, 44]]]]
B = [1, 2, [0, 1], 0, [4, 5, [55, 44, [12, [2, 5], [13, 52]]]]]

# A = [5, 0, 10, [-1, 1]]
# B = [1, -2, [0, 1]]

# A = [4, 0, [0, -5], [-2, 1]]
# B = [1, 0, [0, 1]]

result = add_nested_lists(A, B)
print('Result:', result)
