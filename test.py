string = "UDACITY"

a = str(ord(string[0]))
b = str(ord(string[1]))
c = int(a + b)

print(c)

table = [None]*10

print(table)
p = "pee"
po = 99
table[1] = {p:po}

print(table)
x = 0
for item in table:
    try:
        x = item['pee']
        print(x)
    except:
        pass

