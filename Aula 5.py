lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

lista_animal[0] = 'macaco'
print(lista_animal)

tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)

# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)

#print(lista_animal[1])
#nova_lista = lista_animal + 3
#print(nova_lista)
# soma = 0
# for x in lista:
#     print(x)
#     soma = soma + x
# print(soma)

# if 'lobo' in lista_animal:
#     print('existe um lobo na lista')
# else:
#     print('não existe lobo na lista')
#     lista_animal.append('lobo')
#     print(lista_animal)
# lista_animal.pop()
# print(lista_animal)