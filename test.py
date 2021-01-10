def print_h(n, m):
    count = 0
    while count < n:
        print("значение", count, '- еще нет')
        count = count + m
    else:
        print('значение', count, '- дождались')
print_h(5, 1)



