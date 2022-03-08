conjunto = {1,2,3,4, 5}
conjunto2 = {5,6,7,8}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))
conjunto_diferenca = conjunto.difference(conjunto2)
print('diferença: {}'.format(conjunto_diferenca))
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('difença simeétrica: {}'.format(conjunto_diff_simetrica))
# conjunto = {1,2,3,4}
# conjunto.add(5)
# print(conjunto)