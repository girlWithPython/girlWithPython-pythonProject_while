def print_h(n, m):
    count = 0
    while count < n:
        print("значение", count, '- еще нет')
        count = count + m
    else:
        print('значение', count, '- дождались')
print_h(5, 1)

def print_hello():
    print("дождались")
a, b, c = 16, 32, 1
while a < b:
        print(a, "not yet")
        a+=b
else:
        print("yes!")
print_hello()

