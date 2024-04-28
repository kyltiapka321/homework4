immutable_var = 55555, 7, 'я балбес', 4.0
print(immutable_var)
#immutable_var[2]  = 'я не балбес'  - значения элементов кортежа нельзя изменить потому что они не предназначены для этого, тоесть нее поддерживают изменение по элементам
#print(immutable_var)
mutable_list   = [243, 6, 'хлеб люблю', 78.3]
print(mutable_list)
mutable_list[2] = 'Обажаю хлеб'
print(mutable_list)