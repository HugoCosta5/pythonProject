
lista = [1, 10]

try:
    arquivo = open('teste.txt', 'r')
    divisao = 10 / 1
    numero = lista[1]
    #print('Fechando arquivo')
   # arquivo.close()
    #x = a
except ZeroDivisionError:
    print('Não é possível divisão por 0')
except IndexError:
    print('Erro ao acessar um índice inválido da lista')
except BaseException as ex:
    print(ex)
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()
