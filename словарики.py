#code 1

def dict_zip(employee_numbers, employee_names):
    zipped_values = zip(employee_numbers, employee_names)
    d = dict(zip(employee_numbers, employee_names))
    print(d)

dict_zip([2, 9, 4], ['Vasil', 'Pedro', 'Ivasik'])

#code 2

def dict_(a, b):
    d = {a: b}
    n = d.items()
    for key, value in d.items():
        print(key, 'is', value)

dict_(1, 2)

dict_("War", "peace")

dict_("Freedom", "slavery")

dict_("Ignorance", "strength")


