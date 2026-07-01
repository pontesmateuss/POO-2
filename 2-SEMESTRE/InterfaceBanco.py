import tkinter as tk
from tkinter import messagebox, simpledialog
from ContaBancaria import Endereco, ContaBancaria, Cliente, ContaCorrente, ContaPoupanca, ContaSalario



class BancoApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Sistema Bancário - POO em Python")
        self.janela.geometry("850x400")


        end1 = Endereco("Rua Aviador", 1000, "Cohab", "Ceará-Mirim")
        end2 = Endereco("Rua Bonita", 123, "Centro", "Natal")
        end3 = Endereco("Rua Curricular", 456, "São Geraldo", "Ceará-Mirim")
        end4 = Endereco("Rua Centenárea", 426, "São Geraldo", "Ceará-Mirim")
        end5 = Endereco("Rua Centenárea", 455, "São Geraldo", "Ceará-Mirim")
        end6 = Endereco("Rua Centenárea", 490, "São Geraldo", "Ceará-Mirim")
       
        cliente1 = Cliente("Mateus", "100.200.300-04", end1)
        cliente2 = Cliente("Pedro", "111.222.333-44", end2)
        cliente3 = Cliente("Vitoria", "777.777.777-77", end3)
        cliente4 = Cliente("João", "222.222.222-22", end4)
        cliente5 = Cliente("Isaac", "333.333.333-33", end5)
        cliente6 = Cliente("Maria", "444.444.444-44", end6)

        self.contas = [
            ContaCorrente(cliente1, "1002", 1000.0),
            ContaCorrente(cliente2, "1003", 300.0),
            ContaPoupanca(cliente3, "1004", 20.0),
            ContaPoupanca(cliente4, "1005", 50.0),
            ContaSalario(cliente5, "1006", 100.0, "IFRN"),
            ContaCorrente(cliente6, "1007", 3000.0)
]
       
        self.criar_interface()


    def criar_interface(self):
        titulo = tk.Label(
            self.janela,
            text="Banco Python - Contas Bancárias",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)
        self.frame_contas = tk.Frame(self.janela)
        self.frame_contas.pack()
        self.atualizar_tela()


    def atualizar_tela(self):
        for widget in self.frame_contas.winfo_children():
            widget.destroy()
        for conta in self.contas:
            frame = tk.Frame(
                self.frame_contas,
                borderwidth=2,
                relief="groove",
                padx=10,
                pady=10
            )
            frame.pack(side="left", padx=10, pady=10)


            lbl_titular = tk.Label(
                frame,
                text=conta.get_titular().get_nome(),
                font=("Arial", 14, "bold")
            )

            lbl_tipo = tk.Label(
                frame,
                text=conta.get_tipo_conta(),
                font=("Arial", 10, "italic")
            )
            lbl_tipo.pack()
            
            lbl_titular.pack()


            lbl_numero = tk.Label(
                frame,
                text=f"Conta: {conta.get_numero()}"
            )
            lbl_numero.pack()


            lbl_saldo = tk.Label(
                frame,
                text=f"Saldo: R$ {conta.get_saldo():.2f}",
                font=("Arial", 12)
            )
            lbl_saldo.pack(pady=5)


            btn_depositar = tk.Button(
                frame,
                text="Depositar",
                width=15,
                command=lambda c=conta: self.depositar(c)
            )
            btn_depositar.pack(pady=2)


            btn_sacar = tk.Button(
                frame,
                text="Sacar",
                width=15,
                command=lambda c=conta: self.sacar(c)
            )
            btn_sacar.pack(pady=2)


            btn_transferir = tk.Button(
                frame,
                text="Transferir",
                width=15,
                command=lambda c=conta: self.transferir(c)
            )
            btn_transferir.pack(pady=2)


            btn_dados = tk.Button(
                frame,
                text="Exibir Dados",
                width=15,
                command=lambda c=conta: self.exibir_dados(c)
            )
            btn_dados.pack(pady=2)
    def depositar(self, conta):
        valor = simpledialog.askfloat(
            "Depósito",
            "Digite o valor do depósito:"
        )
        if valor is not None:
            if valor > 0:
                conta.depositar(valor)
                messagebox.showinfo(
                    "Sucesso",
                    "Depósito realizado."
                )
            else:
                messagebox.showerror(
                    "Erro",
                    "Valor inválido."
                )
        self.atualizar_tela()
    def sacar(self, conta):
        valor = simpledialog.askfloat(
            "Saque",
            "Digite o valor do saque:"
        )
        if valor is not None:
            if conta.sacar(valor):
                messagebox.showinfo(
                    "Sucesso",
                    "Saque realizado."
                )
            else:
                messagebox.showerror(
                    "Erro",
                    "Saldo insuficiente ou valor inválido."
                )
        self.atualizar_tela()
    def transferir(self, conta_origem):
        valor = simpledialog.askfloat(
            "Transferência",
            "Digite o valor:"
        )
        if valor is None:
            return
        numero_destino = simpledialog.askstring(
            "Transferência",
            "Digite o número da conta destino:"
        )
        if not numero_destino:
            return
        conta_destino = None
        for conta in self.contas:
            if conta.get_numero() == str(numero_destino):
                conta_destino = conta
                break
        if conta_destino is None:
            messagebox.showerror(
                "Erro",
                "Conta destino não encontrada."
            )
            return
        if conta_origem == conta_destino:
            messagebox.showerror(
                "Erro",
                "Não é possível transferir para a mesma conta."
            )
            return
        if conta_origem.transferir(valor, conta_destino):
            messagebox.showinfo(
                "Sucesso",
                "Transferência realizada."
            )
        else:
            messagebox.showerror(
                "Erro",
                "Saldo insuficiente ou valor inválido."
            )
        self.atualizar_tela()
    def exibir_dados(self, conta):
        dados = conta.exibir_dados()
        cliente = conta.get_titular()
        dados += f"\n\n--- Informações do Cliente ---\n{cliente.exibir_dados()}"
        if ContaBancaria.existe_conta_duplicada():
            dados += (
                "\n\nExistem contas duplicadas."
                f"\nNúmeros duplicados: "
                f"{ContaBancaria.contas_duplicadas()}"
            )
        else:
            dados += "\n\nNão existem contas duplicadas."
        messagebox.showinfo(
            "Dados da Conta",
            dados
        )
if __name__ == "__main__":
    janela = tk.Tk()
    app = BancoApp(janela)
    janela.mainloop()
