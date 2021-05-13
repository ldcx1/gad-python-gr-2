print('Acesta este cursul al 2-lea')

name = 'Ana'
if name:
    print(name)
    print(type(name))
else:
    print('Nu avem definit nici un nume')

first_person = {'Name': 'John'}
second_person = {'Name': 'John'}

if first_person is second_person:
    print('They are pointing to the same memory')
else:
    print('They are not the same')

if first_person == second_person:
    print('They are equal')
else:
    print('They are not the same')

my_str = 'Ana ar\' mere'
# my_str[2] = 't'
print(my_str[2])
print(my_str)

print("""fdshgsdfgsdfg
dfgdsfgsdf
gsdf
g
sdfg
sdf
g
sdf
gsdfhs""")


msg = '{} has {} years'.format('Ion', '37')
msg2 = '{name} has {age} years'.format(name='Maria', age='33')
msg3 = '{1} has {0} years'.format('Maria', '33')

name = 'Ion'
age = 18
msg4 = f'{name} has {age} years'
print(msg4)

l = [1, 2, 3, 'Ana are mere', True, False, None, [4, 5, 6]]
print(l)
l[4] = 55
print(l)

inventar = ['faina', 'drojdie', 'apa', 'sare']
for item in inventar:
    print(item)

for index, value in enumerate(inventar):
    print(f'{index}: {value}')

print(inventar[len(inventar) - 1])
print(inventar[-1])
print(inventar[0:-1:2])
l = [3, 2 , 1 ,4]
print(l)
print(sorted(l))
l.sort()
print(l)

l1 = [2,3,0,9]
l2 = [12,[13,10],4,15]
l3 = l1 + l2
print(l3)
l1.extend(l2)
print(l1)

my_dict = {1: "Home", 2: "Office", 3: "Restaurant"}
for key,val in my_dict.items():
    print(f"{key}: {val}")
print(my_dict[3])
print(my_dict.get(4, 'Nu exista'))

l = [1, 2, 2, 3]
l2 = [1, 9, 9, 3]
print(l)

s1 = set(l)
s2 = set(l2)
print(s1 - s2)
print(s1 & s2)
print(list(s1.intersection(s2)))

