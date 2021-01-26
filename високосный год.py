def leapyear(n):
    assert n % 1 == 0
    if n==0: print("Нулевой год и «нулевой год до н. э.» не существуют согласно григорианскому и юлианскому летоисчислениям")
    elif n<0: print("Гуглу неизвестно, были ли до нашей эры високосные года")
    elif n % 400 == 0: print("Oh, the Leap Year is coming! God bless us!")
    elif (n % 100 != 0) and (n % 4 == 0):
        print("Oh, the Leap Year is coming! God bless us!")
    else:
        print("This year isn't a leap year")

leapyear(-10)

def leapyear_adv(m):
    assert m > 0 and m % 1 == 0
    me_say = "Oh, the Leap Year is coming! God bless us!" if m % 400 == 0 or (m % 100 != 0) and (m % 4 == 0) else "This year isn't a leap year"
    print(me_say)

leapyear_adv(1300)

