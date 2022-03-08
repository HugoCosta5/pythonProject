a = int(input('primeiro bimestre: '))
while a > 10:
    a = int(input('você digitou errado. Primeiro bimenstre: '))
b = int(input('segundo bimenstre: '))
while b > 10:
    b = int(input('você digitou errado. Segundo bimenstre: '))
c = int(input('terceiro semestre: '))
while c > 10:
    c = int(input('você digitou errado. Terceiro bimenstre: '))
d = int(input('quarto semestre: '))
while d > 10:
    d = int(input('você digitou errado. Quarto bimenstre: '))

media = ((a+b+c+d)/ 4)
print('média: {}' .format(media))

# nota = int(input('entre com a nota'))
# while nota > 10:
#     nota = int(input('entre com a nota: '))

# a = 0
# while a <= 10:
#     print(a)
#     a = a+1

# a = int(input('entre com o valor: '))
# for num in range(a+1):
#     div = 0
#     for x in range (1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div = div +1
#     if div == 2:
#         print(num)

    # else:
    #     print('número não é primo' .format(a))