x = 12

if x == 25:
    print("YES 25")
else:
    print("NOT 25")

if x <= 4:
    print("Too small age")
elif (x > 4) and (x < 12):
    print("Kid age")
elif (x >= 12) and (x < 19):
    print("Teen ager")
else:
    print("Too old age")

cars = ['lada', 'moskvich', 'volga', 'zapor']

ruscar = ['lada', 'moskvich', 'volga']

for car in cars:
    if car in ruscar:
        print("Rus car: ", car)
    else:
        print("Bad car:", car)