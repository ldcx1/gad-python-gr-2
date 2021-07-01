import copy

print("Memory savers")
print("-" * 80)

my_lambda = lambda x, y: x + y
rez = my_lambda(1, 2)
print(rez)

players = [
    {
        'first_name': 'Jhon',
        'last_name': 'Doe',
        'rank': 3
    },
    {
        'first_name': 'Kevin',
        'last_name': 'McDonald',
        'rank': 1
    },
    {
        'first_name': 'Brad',
        'last_name': 'Kelvin',
        'rank': 22
    }
]

print(players)
sorted_palyers = sorted(players, key=lambda player: player['rank'])
print(sorted_palyers)


def check_top_3_player(player):
    updated_player = copy.deepcopy(player)
    updated_player["is_top_3"] = True if player['rank'] <= 3 else False
    return updated_player


top_players = list(map(check_top_3_player, players))
print(top_players)

all_mcdonalds = list(filter(lambda player: player["last_name"] == 'McDonald', players))
print(all_mcdonalds)

letters = ['a', 'b', 'c', 'd']
numbers = ['1', '2', '3']

print(list(zip(letters, numbers)))
for l, n in zip(letters, numbers):
    print(n, l)

my_numbers = [1, 2, 3, 4, 5]
squared_numbers = [item ** 2 for item in my_numbers if item % 2 == 0]
print(squared_numbers)
