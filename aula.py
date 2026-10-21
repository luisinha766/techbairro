#class cachorro:
#    def __init__(self, nome, raca):
#        self.nome = nome 
#        self.raca = raca
#
#    def latir (self):
#        print(f"{self.nome} (um{self.raca}) esta latindo: au au !")
#
#rex = cachorro ("rex, "vira-lata"³#)
#bidu = cachorro("bidu", "poodle")³#
#³#
#rex.latir()³#
#bidu.latir()³#

class cliente:
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def resumo(self):
        return f"{self.nome}- {self.telefone}- {self.email}- {self.endereco}"

cliente_teste = cliente("ana sousa", "11987654321", "ana@techbairro.com", "ruaA,123")
#print ( cliente_teste.nome)
#print(cliente_teste.telefone)
print(cliente_teste.resumo())

cliente = {campo}
