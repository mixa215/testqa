a = ['Skyrim', 'GTA', 'Sims', 'стоп', 'Mafia']
i = 0
while i < len(a):
    if a[i] == 'стоп' or a[i] == 'хватит' or a[i] == 'достаточно':
        break
    i+=1
print(i)
