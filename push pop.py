ret = []
tyu = []
new = 0
Gorodok = 0
Azeke = input('Длина очереди: ')
for a in range(int(Azeke)):
name = input('ксго или дота : ')
if (int(name) == 2):
Gorodok = Gorodok + 1
else:
ret.insert(new, 1)
new = new + 1

for a in range(int(Azeke)):
if new == 0:
for a in range(Gorodok):
print('бедный ')
tyu.append('бедный')
break
print('Богатый ')
new = new - 1
tyu.append('Богатый')

print(tyu)
