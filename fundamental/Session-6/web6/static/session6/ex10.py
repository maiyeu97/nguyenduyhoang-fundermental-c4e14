get_even_list = [1, 4, 5, -1, 10]
def is_even(l):
    even_list = []
    for n in l:
        if n % 2 == 0:
            even_list.append(n)
            return even_list
even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
