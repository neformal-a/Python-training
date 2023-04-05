numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]
new_numbers = []

for val in numbers:

    try:
        # the first if is redundant
        if type(val) is int:
            new_numbers.append(val)
        # can be also replaced with the catching one more exception
        elif val is None:
            new_numbers.append(0)
        else:
            new_numbers.append(int(val))
    except ValueError:
        pass

print('Min value', min(new_numbers))
print('Max value', max(new_numbers))