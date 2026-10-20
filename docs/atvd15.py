
import tkinter as tk

class Cliente:
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
    def resumo(self):
        return f"{self.nome} | {self.telefone} | {self.email} | {self.endereco}"
clientes = []
def mostrar_erro(mensagem_texto):
    mensagem.config(
        text=mensagem_texto,
        fg="red"
    )
def validar_telefone(event):
    telefone = entradas["Telefone"].get()
    if telefone != "" and not telefone.isdigit():
        mostrar_erro("O telefone deve conter apenas números.")
    else:
        mensagem.config(text="")
def validar_email(event):
    email = entradas["E-mail"].get()
    if email != "" and ("@" not in email or "." not in email):
        mostrar_erro("Digite um E-mail válido.")
    else:
        mensagem.config(text="")
def salvar():
    nome = entradas["Nome"].get()
    telefone = entradas["Telefone"].get()
    email = entradas["E-mail"].get()
    endereco = entradas["Endereço"].get()

    mensagem.config(text="")

    if nome == "":
        mostrar_erro("Preencha o campo Nome.")
        return

    if telefone == "":
        mostrar_erro("Preencha o campo Telefone.")
        return

    if not telefone.isdigit():
        mostrar_erro("O telefone deve conter apenas números.")
        return

    if email == "":
        mostrar_erro("Preencha o campo E-mail.")
        return

    if "@" not in email or "." not in email:
        mostrar_erro("Digite um E-mail válido.")
        return

    if endereco == "":
        mostrar_erro("Preencha o campo Endereço.")
        return

    cliente = Cliente(
        nome,
        telefone,
        email,
        endereco
    )

    clientes.append(cliente)

    mensagem.config(
        text="Cliente cadastrado com sucesso!",
        fg="green"
    )
    for entrada in entradas.values():
        entrada.delete(0, tk.END)

def cancelar():

    for entrada in entradas.values():
        entrada.delete(0, tk.END)

    mensagem.config(text="")


def abrir_consulta():

    consulta = tk.Toplevel(janela)

    consulta.title("TechBairro — Consulta de Clientes")
    consulta.geometry("600x300")
    consulta.resizable(False, False)

    tk.Label(
        consulta,
        text="Clientes cadastrados",
        font=("Arial", 14, "bold")
    ).pack(pady=10)

    area_lista = tk.Frame(consulta)
    area_lista.pack(pady=5)

    lista = tk.Listbox(
        area_lista,
        width=80,
        height=10
    )

    lista.grid(
        row=0,
        column=0
    )

    scrollbar = tk.Scrollbar(
        area_lista,
        orient="vertical",
        command=lista.yview
    )

    scrollbar.grid(
        row=0,
        column=1,
        sticky="ns"
    )

    lista.config(
        yscrollcommand=scrollbar.set
    )

    for cliente in clientes:
        lista.insert(
            tk.END,
            cliente.resumo()
        )

janela = tk.Tk()

janela.title("TechBairro — Cadastro de Cliente")
janela.geometry("480x420")
janela.resizable(False, False)

cabecalho = tk.Frame(
    janela,
    bg="#502c42"
)

cabecalho.pack(
    side="top",
    fill="x"
)

tk.Label(
    cabecalho,
    text="Cadastro de Cliente",
    fg="white",
    bg="#56295a",
    font=("Arial", 14, "bold"),
    pady=12
).pack()


form = tk.Frame(janela)

form.pack(pady=20)

campos = [
    "Nome",
    "Telefone",
    "E-mail",
    "Endereço"
]

entradas = {}


for i, campo in enumerate(campos):

    tk.Label(
        form,
        text=f"{campo}:"
    ).grid(
        row=i,
        column=0,
        sticky="e",
        padx=5,
        pady=6
    )

    entrada = tk.Entry(
        form,
        width=30
    )

    entrada.grid(
        row=i,
        column=1,
        padx=5,
        pady=6
    )

    entradas[campo] = entrada


mensagem = tk.Label(
    janela,
    text="",
    font=("Arial", 10, "bold")
)

mensagem.pack(pady=2)

entradas["Telefone"].bind(
    "<KeyRelease>",
    validar_telefone
)
entradas["E-mail"].bind(
    "<KeyRelease>",
    validar_email
)

botoes = tk.Frame(janela)

botoes.pack(pady=10)


tk.Button(
    botoes,
    text="Salvar",
    width=12,
    command=salvar
).grid(
    row=0,
    column=0,
    padx=5
)


tk.Button(
    botoes,
    text="Cancelar",
    width=12,
    command=cancelar
).grid(
    row=0,
    column=1,
    padx=5
)


tk.Button(
    botoes,
    text="Consultar",
    width=12,
    command=abrir_consulta
).grid(
    row=0,
    column=2,
    padx=5
)


versao = tk.Label(
    janela,
    text="v1.0",
    fg="gray"
)

versao.place(
    relx=0.97,
    rely=0.97,
    anchor="se"
)

janela.mainloop()