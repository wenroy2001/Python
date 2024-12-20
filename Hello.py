def print_pyramid(levels):
    for i in range(levels):
        print(' ' * (levels - i - 1) + '*' * (2 * i + 1))

print_pyramid(5)