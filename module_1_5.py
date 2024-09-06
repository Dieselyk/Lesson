immutable_var = ('a', 'b', 1, 2)
print(immutable_var)

# кортеж относится к неизменяемым типам данных, по этому мы не можем его изменить, но можем ввести в него, к примеру, список и изменять этот список.

mutable_list = ['a', 'b', 1, 2]
print(mutable_list)
mutable_list.append('car')
print(mutable_list)
mutable_list[1] = 'home'
print(mutable_list)