mn = input()
if len(mn) > 10 or not mn.isdigit():
    print("Untransformable")

result = []

for i in mn:
    i = int(i)
    if i <= 5:
        parent_morse = '-' * 5
        result.append(parent_morse.replace('-', '.', i))
    elif i > 5:
        parent_morse = '.' * 5
        i -= 5
        result.append(parent_morse.replace('.', '-', i))

print(*result)