boxes = int(input('Enter the number of boxes: '))
wanted_output = input('Enter 1 for total or 2 for last: ')

if wanted_output == '1':
    total = 1
    for _ in range(boxes):
        total *= 2
    else:
        print(total)
else:
    result = 1 * 2 ** (boxes - 1)
    print(result) # sup nigga
