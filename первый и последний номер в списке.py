def list_(s):
   lst_ = list(str(s))
   print(lst_)
   print("первый элемент списка: ", lst_[0], ",", "последний элемент списка: ", lst_[-1])
list_(590765555)

def list(s):
   s = str(s)
   lst_ = s.split(' ')
   print(lst_)
   print("первый элемент списка: ", lst_[0], ",", "последний элемент списка: ", lst_[-1])
list('5 90 76 5555')


