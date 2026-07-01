from typing import List



class Endereco:
    def __init__(self, rua: str, numero: int, bairro: str, cidade: str):
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade
    def get_rua(self) -> str:
        return self.__rua
    def get_numero(self) -> int:
        return self.__numero
    def get_bairro(self) -> str:
        return self.__bairro
    def get_cidade(self) -> str:
        return self.__cidade
    def exibir_dados(self) -> str:
        return f"{self.__rua}, {self.__numero} - {self.__bairro}, {self.__cidade}"



class Cliente:
    def __init__(self, nome: str, cpf: str, endereco: Endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__contas: List['ContaBancaria'] = []

    def get_nome(self) -> str:
        return self.__nome
    
    def get_cpf(self) -> str:
        return self.__cpf
    
    def get_endereco(self) -> Endereco:
        return self.__endereco
    
    def adicionar_conta(self, conta: 'ContaBancaria') -> None:
        if conta not in self.__contas:
            self.__contas.append(conta)

    def exibir_dados(self) -> str:
        return f"Nome: {self.__nome}\nCPF: {self.__cpf}\nEndereço: {self.__endereco.exibir_dados()}"



class ContaBancaria:
    numeros_contas = []
    def __init__(self, cliente: Cliente, numero: str, saldo: float):
        self.__cliente = cliente
        self.__numero = str(numero)
        if saldo < 0:
            self.__saldo = 0.0
        else:
            self.__saldo = float(saldo)
        ContaBancaria.numeros_contas.append(self.__numero)
        cliente.adicionar_conta(self)
    def get_titular(self) -> Cliente:
        return self.__cliente
    
    def get_numero(self) -> str:
        return self.__numero
    
    def get_saldo(self) -> float:
        return self.__saldo
    
    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor: float) -> bool:
        if valor > 0 and self.__saldo >= valor:
            self.__saldo -= valor
            return True
        return False
    
    def transferir(self, valor: float, conta_destino: 'ContaBancaria') -> bool:
        if valor > 0 and self.sacar(valor):
            conta_destino.depositar(valor)
            return True
        return False
    
    def exibir_dados(self) -> str:
        return (
            f"Titular: {self.__cliente.get_nome()}\n"
            f"Conta: {self.__numero}\n"
            f"Saldo: R$ {self.__saldo:.2f}"
        )


    @classmethod
    def existe_conta_duplicada(cls):
        return len(cls.numeros_contas) != len(set(cls.numeros_contas))


    @classmethod
    def contas_duplicadas(cls):
        duplicadas = []
        for numero in cls.numeros_contas:
            if cls.numeros_contas.count(numero) > 1 and numero not in duplicadas:
                duplicadas.append(numero)
        return duplicadas



class ContaCorrente(ContaBancaria): 
    def __init__(self, cliente: Cliente, numero: str, saldo: float):
        super().__init__(cliente, numero, saldo)

    def sacar(self, valor: float) -> bool:
        return super().sacar(valor)
    
    def cobrar_tarifa():
        return
    
    def exibir_dados(self) -> str:
        return super().exibir_dados()
    
    def get_tipo_conta():
        return



class ContaPoupanca(ContaBancaria):
    def __init__(self, cliente: Cliente, numero: str, taxa_rendimento: float):
        super().__init__(cliente, numero, taxa_rendimento)

    def sacar(valor: float):
        return
    
    def render_juros():
        return
    
    def exibir_dados(self) -> str:
        return super().exibir_dados()
    
    def get_tipo_conta():
        return


    
class ContaSalario(ContaBancaria):
    def __init__(self, empresa: Cliente, saques_realizados: str, limite_saques: float):
        def __init__( empresa: str, saques_realizados: int, limite_saques: int):
            self.__empresa = empresa
            self.__saques_realizados - saques_realizados
            self.__limite_saques = limite_saques

    def receber_salario(valor: float):
        return
    
    def sacar(self, valor: float) -> bool:
        return super().sacar(valor)
    
    def depositar(self, valor: float) -> None:
        return super().depositar(valor)
    
    def transferir(self, valor: float, conta_destino: ContaBancaria) -> bool:
        return super().transferir(valor, conta_destino)
    
    def exibir_dados(self) -> str:
        return super().exibir_dados()

    def get_tipo_conta():
        return