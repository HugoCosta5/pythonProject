a = int(input('primeiro bimestre: '))
if a > 10:
    a = int(input('você digitou errado. Primeiro bimenstre: '))
b = int(input('segundo bimenstre: '))
if b > 10:
    b = int(input('você digitou errado. Segundo bimenstre: '))
c = int(input('terceiro semestre: '))
if c > 10:
    c = int(input('você digitou errado. Terceiro bimenstre: '))
d = int(input('quarto semestre: '))
if d > 10:
    d = int(input('você digitou errado. Quarto bimenstre: '))

media = ((a+b+c+d)/ 4)
print('média: {}' .format(media))

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('media: {}' . format(media))
# else:
#     print('foi digitado algum valor errado')

# a = int(input('entre com o primeiro valor: '))
# b = int(input('entre com o segundo valor: '))
# resto_a = a % 2 # <-- para saber se é par
# resto_b = b % 2 # <-- para saber se é par
# if resto_a == 0 or resto_b == 0:
#     print('foi digitado um número par')
# else:
#     print('nenhum número par foi digitado')

# a = int (input('primeiro valor'))
# b = int(input ('segundo valor'))
# c = int(input('terceiro valor'))
# if a > b and a > c:
#     print('o maior valor é {}' .format(a))
# elif b > a and b > c:
#     print('o maior número é {}' .format(b))
# else:
#     print('o maior número é {}' .format(c))
# print('final do programa')