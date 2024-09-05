def calculate_structure_sum(data):
    sum = 0
    for i in data:
        if isinstance(i, int):
            sum += i
        elif isinstance(i, str) and len(i) > 0:
            sum += len(i)
        elif isinstance(i, (list, tuple, set)):
            sum += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            sum += calculate_structure_sum(*i.keys())
            sum += calculate_structure_sum(*i.values())
    return sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(*data_structure)
print(result)