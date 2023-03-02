cities = ['moscow', 'nizgny', 'spb', 'donetsk']

print(cities)
print(len(cities))
print(cities[0], " - ", cities[3])
print(cities[-1])
print(cities[-2].title())
cities[2] = 'tula'
print(cities)
cities.append('mariupol')
print(cities)
cities.insert(1, 'herson')
print(cities)
del cities[-1]
print(cities)
cities.remove('tula')
print(cities)
some_city = cities.pop()
print("Removed by pop: ", some_city)
cities.sort(reverse=1)
cities.reverse()
print(cities)