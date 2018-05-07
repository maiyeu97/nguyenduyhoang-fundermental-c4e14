teen_dict = {
    'eny' : 'Em nguoi yeu',
    'any' : 'Anh nguoi yeu',
    'ns' : 'noi',
    'r' : 'roi (trong tu xong roi)'
}

while True:
    for key, value in teen_dict.items():
        print(key, end=' ')
        print()
    code = input("enter a code: ").lower()
    if code in teen_dict:
        print(code)
        print(teen_dict[code])
    else:
        choice = input("Not found,do you want to contriboot (y/n)?").lower()
        if choice == 'y':
            translasion = input("Translasion:")
            teen_dict[code] = translasion
