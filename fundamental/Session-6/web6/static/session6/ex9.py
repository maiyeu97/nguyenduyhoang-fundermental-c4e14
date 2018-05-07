get_even_list = [1, 4, 5, -1, 10]
def is_even(l):
    even_list = []
    for n in l:
        if n % 2 == 0:
            even_list.append(n)
    print(even_list)
    # return even_list
is_even(get_even_list)
