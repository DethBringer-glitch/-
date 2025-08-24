dict = {"hp": 10, "exp": 5, "mana": 15}
levels = ["lvl 1", "lvl 2", "lvl 3"]
for x in levels:
    print(x)
    for j in dict:
        print(f'{j} : {dict[j]}')
        if j == "hp":
            dict[j]+=10
        elif j == "exp":
            dict[j] += 5
        else:
            dict[j]+= 15