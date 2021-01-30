def dict_(a, b):
    d = {a: b}
    n = d.items()
    for key, value in d.items():
        print(key, 'is', value)

dict_(1, 2)

dict_(11, 22)

dict_(111, 222)

dict_("War", "peace")

dict_("Freedom", "slavery")

dict_("Ignorance", "strength")


