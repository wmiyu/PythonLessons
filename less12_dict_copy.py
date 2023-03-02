enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'yellow-blue',
    'hp': 100,
    'name': 'Mudillo',
    'awards': ['za stalina', 'za lenina']
}

all_enemies = []

for x in range(0, 10):
    nmy = enemy.copy()
    nmy['name'] += str(x)
    nmy['loc_x'] += 10 + x
    all_enemies.append(nmy)

all_enemies[2]['hp'] = 30

for en in all_enemies:
    print(en)