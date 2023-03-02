
cars = ['lada', 'moskvich', 'volga', 'zapor', 'lada', 'moskvich', 'volga2', 'zapor2']

if 'lada' in cars:
    print("Russian car found")

numbers = list(range(1, 4))
for x in cars:
    [print(x.upper())]

print(numbers)

for n in numbers:
    n = n * 6
    print(n, sep='-', end=' ')

print("\nMax is :" , max(numbers))

old_cars = cars[-2:]
print(old_cars)