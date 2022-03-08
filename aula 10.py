from datetime import date, time, datetime

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%H:%M:%S'))
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça' , 'Quarta' , 'Quinta', 'Sexta' , 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%d/%m/%Y')
    print(data_atual_str)

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)

if __name__ =='__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()