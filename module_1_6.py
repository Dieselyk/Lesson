my_dict = {'Den': 1995, 'Max': 2002}
print(my_dict)
print(my_dict['Den'])
my_dict.update({'Tom': 1992,
                'Tim': 1999})
a = my_dict.pop('Max')
print(a)
print(my_dict)


my_set = {1, 2, 3, 1, 1, 'Tom', 5, 4, 4}
print(my_set)
my_set.update({6, 9})
my_set.discard(2)
print(my_set)
