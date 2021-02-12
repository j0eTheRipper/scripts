def is_palendrom(string):
    string = list(string)

    if string[::-1] == string:
        return 'OK'
    else:
        for i in range(len(string)):
            temp_string = string
            letter = temp_string[i]
            temp_string = temp_string.pop(i)
            if temp_string[::-1] == temp_string:
                return 'remove one'
            else:
                temp_string.insert(i, letter)
        else:
            return 'not possible'
