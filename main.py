# Basic Triangle
for i in range(1, 6):
    print('*' * i)

# Upside-down Triangle
for i in range(5, 0, -1):
    print('*' * i)

# Number Triangle
for i in range(5, 0, -1):
    print(''.join(str(j) for j in range(1, i + 1)))

# Numbered Row Triangle
for i in range(1, 6):
    print(str(i) * i)

# Centered Triangle
for i in range(1, 10, 2):
    print(' ' * ((9 - i) // 2) + '*' * i)

# Centered Numbered Triangle
for i in range(1, 10, 2):
    print(' ' * ((9 - i) // 2) + str(i) * i)

# Upside Down Counting Down Triangle
for i in range(5, 0, -1):
    print(''.join(str(j) for j in range(i, 0, -1)))

# Empty Rectangle
for i in range(5):
    if i == 0 or i == 4:
        print('*' * 5)
    else:
        print('*' + ' ' * 3 + '*')

# Non-Empty Rectangle
for i in range(5):
    if i == 0 or i == 4:
        print('*' * 5)
    else:
        print('*' + str(i % 2 + 1) * 3 + '*')

