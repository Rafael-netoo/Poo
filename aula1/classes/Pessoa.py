class Pessoa:
    def __init__(self,nome,peso,idade, dormindo = False,falando = False,comendo = False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.dormindo = dormindo
        self.comendo = comendo
        self.falando = falando
    def comer(self,comida, bebida):

        if(self.falando == True):
            print(f"{self.nome} está falando e não pode comer agora")
        elif(self.dormindo == True):
            print(f"{self.nome} está dormindo e não pode comer agora")
        elif(self.comendo == True):
            print(f"{self.nome} já está comendo")
        else:
            self.comendo = True
            print(f"{self.nome} esta comendo {comida} e {bebida}")

    def falar(self, fala):
         if(self.falando == True):
            print(f"{self.nome} Já está falando")
         elif(self.dormindo == True):
            print(f"{self.nome} está dormindo e não pode falar agora")
         elif(self.comendo == True):
            print(f"{self.nome} está comendo agora e não pode falar")
         else:
            print(f'{self.nome} : {fala}')
            self.falando = True

    def dormir(self):
       if(self.falando == True):
            print(f"{self.nome} está falando e não pode dormir")
       elif(self.dormindo == True):
            print(f"{self.nome} já está dormindo")
       elif(self.comendo == True):
            print(f"{self.nome} está comendo e não pode dormir agora")
       else:
            print(f'{self.nome} : dormindo')
            self.dormindo = True

    def desativarDormir(self):
      if (self.dormindo == False):
          print(f"{self.nome} não está dormindo!")
      else:
          self.dormindo = False
          print(f"{self.nome} acordou!")
    def desativarFalar(self):
        if(self.falando == False):
            print(f"{self.nome} não está falando!")
        else:
            self.falando = False
            print(f"{self.nome} parou de falar!")
    def desativarComer(self):
        if(self.comendo == False):
            print(f"{self.nome} não está comendo!")
        else:
            self.comendo == False
            print(f"{self.nome} parou de comer!")