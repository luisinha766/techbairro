
import tkinter as tk

janela = tk.Tk()
janela.title("TechBairro — Cadastro de Cliente")
janela.geometry("500x350")
janela.configure(bg="#FFF0F5")

topo = tk.Frame(janela, bg="#E91E63")
topo.pack(side="top", fill="x")

tk.Label(
    topo,
    text="Cadastro de cliente",
    fg="white",
    bg="#E91E63",
    pady=10
).pack()


form = tk.Frame(janela, bg="#FFF0F5")
form.pack(pady=20)

campos = ["Nome", "Telefone", "E-mail", "Endereço"]

entradas = {}

for i, campo in enumerate(campos):

    tk.Label(
        form,
        text=f"{campo}:",
        bg="#FFF0F5",
        fg="#C2185B"
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


clientes = []

clientes_cadastrados = 0


def limpar_campos():

    for entrada in entradas.values():

        entrada.delete(0, tk.END)


def salvar_nome():

    nome_digitado = entradas["Nome"].get().strip()

    if nome_digitado == "":
        status.config(
            text="O campo nome é obrigatório.",
            fg="#E53935"
        )

        return False

    return True


def salvar_telefone():

    telefone_digitado = entradas["Telefone"].get().strip()

    if not telefone_digitado.isdigit():
        status.config(
            text="Deve conter apenas números.",
            fg="#E53935"
        )

        return False

    return True


def salvar_email():

    email_digitado = entradas["E-mail"].get().strip()

    if "@" not in email_digitado or "." not in email_digitado.split("@")[-1]:
        status.config(
            text="O e-mail digitado não é válido.",
            fg="#E53935"
        )

        return False

    return True


def salvar_cliente():

    global clientes_cadastrados

    if not salvar_nome():
        return

    if not salvar_telefone():
        return

    if not salvar_email():
        return

    cliente = {
        "Nome": entradas["Nome"].get().strip(),
        "Telefone": entradas["Telefone"].get().strip(),
        "E-mail": entradas["E-mail"].get().strip(),
        "Endereço": entradas["Endereço"].get().strip()
    }

    clientes.append(cliente)

    clientes_cadastrados += 1

    contador.config(
        text=f"Clientes cadastrados: {clientes_cadastrados}"
    )

    status.config(
        text="Cliente cadastrado com sucesso!",
        fg="#D81B60"
    )

    print(
        f"O botão Salvar foi clicado, "
        f"Nome: {cliente['Nome']}"
    )

    limpar_campos()


def cancelar():

    limpar_campos()

    status.config(
        text="Cadastro cancelado.",
        fg="#E53935"
    )


def abrir_consulta():

    consulta = tk.Toplevel(janela)
    consulta.title("Consulta de Clientes")
    consulta.geometry("420x300")
    consulta.configure(bg="#FFF0F5")

    lista = tk.Listbox(
        consulta,
        width=55
    )

    lista.pack(
        side="left",
        padx=(10, 0),
        pady=10,
        fill="both",
        expand=True
    )

    scrollbar = tk.Scrollbar(consulta)

    scrollbar.pack(
        side="right",
        fill="y",
        pady=10
    )

    lista.config(
        yscrollcommand=scrollbar.set
    )

    scrollbar.config(
        command=lista.yview
    )

    if not clientes:

        lista.insert(
            tk.END,
            "Nenhum cliente cadastrado"
        )

    else:

        for cliente in clientes:

            lista.insert(
                tk.END,
                f"Nome: {cliente['Nome']} | "
                f"Telefone: {cliente['Telefone']} | "
                f"E-mail: {cliente['E-mail']} | "
                f"Endereço: {cliente['Endereço']}"
            )


botoes = tk.Frame(janela, bg="#FFF0F5")

botoes.pack(pady=10)
tk.Button(
    botoes,
    text="Salvar",
    command=salvar_cliente,
    width=12,
    bg="#E91E63",
    fg="white"
).grid(
    row=0,
    column=0,
    padx=5
)
tk.Button(
    botoes,
    text="Cancelar",
    command=cancelar,
    width=12,
    bg="#E53935",
    fg="white"
).grid(
    row=0,
    column=1,
    padx=5
)
tk.Button(
    botoes,
    text="Consultar Clientes",
    command=abrir_consulta,
    width=18,
    bg="#C2185B",
    fg="white"
).grid(
    row=0,
    column=2,
    padx=5
)
status = tk.Label(
    janela,
    text="",
    bg="#FFF0F5",
    fg="#E53935"
)

status.pack()
contador = tk.Label(
    janela,
    text="Clientes cadastrados: 0",
    bg="#FFF0F5",
    fg="#C2185B"
)

contador.pack()
versao = tk.Label(
    janela,
    text="v1.0",
    bg="#FFF0F5",
    fg="#E53935"
)
versao.place(
    relx=0.97,
    rely=0.97,
    anchor="se"
)
janela.mainloop()
