class Pessoa:
    def __init__(self,nome,peso,idade, dormindo = False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.dormindo = dormindo
    def comer(self,comida, bebida):
        print(f'{self.nome} foi comer {comida} e beber {bebida}')
    def falar(self, fala):
        print(f'{self.nome} : {fala}')
    def dormir(self):
        self.dormindo = True
        print(f'{self.nome} : Dormindo({self.dormindo})')