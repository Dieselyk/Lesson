def print_params(a=1, b='', c=True):
    print(a, b, c)


values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
print_params(b=25)
print_params(c=[1, 2, 3])


values_list = [32, 'имя', [1, 2]]
values_dict = {'a': 1, 'b': 2, 'c': 3}
print_params(*values_list)
print_params(**values_dict)


values_list_2 = [32, 'имя']
print_params(*values_list_2)