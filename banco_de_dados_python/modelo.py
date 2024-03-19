class Pessoa:
    def __init__(self, cpf, nome, nascimento, usa_oculos):
        self.cpf=cpf
        self.nome=nome
        self.nascimento=nascimento
        self.usa_oculos= usa_oculos

class Marca:
    def __init__(self, nome, sigla):
        self.id=None
        self.nome=nome
        self.sigla=sigla

class Veiculo:
    def __init__(self,placa, ano, cor, motor, proprietario, marca):
        self.placa=placa
        self.ano=ano
        self.cor=cor
        self.motor=motor
        self.proprietario=proprietario
        self.marca=marca
        