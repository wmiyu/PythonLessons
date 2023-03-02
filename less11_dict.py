enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'yellow-blue',
    'hp': 100,
    'name': 'Mudillo',
}

print(enemy)

print("Location X = " + str(enemy['loc_x']))
print("Location Y = " + str(enemy['loc_y']))
print("Target Name = " + enemy['name'])

enemy['rank'] = 'admiral'
print(enemy)

del enemy['rank']
print(enemy)

enemy['loc_x'] = enemy['loc_x'] + 40
enemy['hp'] = enemy['hp'] - 95
if enemy['hp'] < 10:
    enemy['color'] = 'grey'
print(enemy.keys())
print(enemy.values())