
import tkinter as tk
class Cliente:
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
class GerenciadorClientes:
    def __init__(self):
        self.clientes = []

    def adicionar(self, cliente):
        self.clientes.append(cliente)

    def listar(self):
        return self.clientes

    def atualizar(self, indice, novo_cliente):
        print("Atualizar ainda não foi implementado.")

    def remover(self, indice):
        print("Remover ainda não foi implementado.")
gerenciador = GerenciadorClientes()
janela = tk.Tk()
janela.title("TechBairro — Cadastro de Cliente")
janela.geometry("480x420")
janela.resizable(False, False)
cabecalho = tk.Frame(janela, bg="#2c3e50")
cabecalho.pack(fill="x")
tk.Label(
    cabecalho,
    text="Cadastro de Cliente",
    fg="white",
    bg="#2c3e50",
    font=("Arial", 14, "bold"),
    pady=12
).pack()
form = tk.Frame(janela)
form.pack(pady=20)
campos = ["Nome", "Telefone", "E-mail", "Endereço"]
entradas = {}
for i, campo in enumerate(campos):
    tk.Label(form, text=f"{campo}:").grid(
        row=i, column=0, padx=5, pady=6
    )

    entrada = tk.Entry(form, width=30)
    entrada.grid(row=i, column=1, padx=5, pady=6)

    entradas[campo] = entrada
mensagem = tk.Label(
    janela,
    text="",
    fg="red"
)
mensagem.pack()
def salvar():
    nome = entradas["Nome"].get()
    telefone = entradas["Telefone"].get()
    email = entradas["E-mail"].get()
    endereco = entradas["Endereço"].get()

    mensagem.config(text="")

    if nome == "":
        mensagem.config(text="Digite o nome.")
        return

    if telefone == "" or not telefone.isdigit():
        mensagem.config(text="Digite um telefone válido.")
        return

    if email == "" or "@" not in email or "." not in email:
        mensagem.config(text="Digite um e-mail válido.")
        return

    if endereco == "":
        mensagem.config(text="Digite o endereço.")
        return

    cliente = Cliente(nome, telefone, email, endereco)
    gerenciador.adicionar(cliente)

    mensagem.config(
        text="Cliente cadastrado com sucesso!",
        fg="green"
    )

    for entrada in entradas.values():
        entrada.delete(0, tk.END)
def abrir_consulta():
    consulta = tk.Toplevel(janela)
    consulta.title("Consulta de Clientes")
    consulta.geometry("480x420")
    tk.Label(
        consulta,
        text="Clientes cadastrados",
        bg="#2c3e50",
        fg="white",
        font=("Arial", 14, "bold"),
        pady=12
    ).pack(fill="x")

    clientes = gerenciador.listar()

    if not clientes:
        tk.Label(
            consulta,
            text="Nenhum cliente cadastrado."
        ).pack(pady=20)
        return

    for cliente in clientes:
        tk.Label(
            consulta,
            text=f"Nome: {cliente.nome}\n"
                 f"Telefone: {cliente.telefone}\n"
                 f"E-mail: {cliente.email}\n"
                 f"Endereço: {cliente.endereco}",
            justify="left"
        ).pack(pady=8)
botoes = tk.Frame(janela)
botoes.pack(pady=10)
tk.Button(
    botoes,
    text="Salvar",
    width=12,
    command=salvar
).grid(row=0, column=0, padx=5)

tk.Button(
    botoes,
    text="Cancelar",
    width=12,
    command=lambda: janela.destroy()
).grid(row=0, column=1, padx=5)
tk.Button(
    botoes,
    text="Consultar",
    width=12,
    command=abrir_consulta
).grid(row=0, column=2, padx=5)
tk.Label(
    janela,
    text="v1.0",
    fg="gray"
).place(
    relx=0.97,
    rely=0.97,
    anchor="se"
)

janela.mainloop()
