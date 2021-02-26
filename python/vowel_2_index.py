def vowel_2_index(string):
    vowels = {'a','e','i','o','u'}
    string = list(string)
    for i in range(len(string)):
        if string[i] in vowels:
            string[i] = i

    return ''.join(string)
