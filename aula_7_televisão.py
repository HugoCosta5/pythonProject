class Televisão:
    def __init__(self):
        self.ligada = False

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

televisao = Televisão()
print('televisão está ligada: {}'.format(televisao.ligada))
televisao.power()
print(televisao.ligada)
televisao.power()
print('televisão está ligada: {}'.format(televisao.ligada))