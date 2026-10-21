
import tkinter as tk
from tkinter import messagebox

clientes = []

VERMELHO_ESCURO = "#8B0000"
VERMELHO = "#E63946"
ROSA = "#FF69B4"
ROSA_CLARO = "#FFB6C1"
BRANCO = "#FFFFFF"


def cadastrar_cliente():
    nome = entrada_nome.get()
    telefone = entrada_telefone.get()
    email = entrada_email.get()
    endereco = entrada_endereco.get()

    if nome == "" or telefone == "" or email == "" or endereco == "":
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos."
        )
        return

    cliente = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "endereco": endereco
    }

    clientes.append(cliente)

    messagebox.showinfo(
        "Sucesso",
        "Cliente cadastrado com sucesso!"
    )

    entrada_nome.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_endereco.delete(0, tk.END)


def abrir_consulta():
    janela_consulta = tk.Toplevel(janela)

    janela_consulta.title("TechBairro - Consulta de Clientes")
    janela_consulta.geometry("800x400")
    janela_consulta.configure(bg=VERMELHO_ESCURO)

    titulo_consulta = tk.Label(
        janela_consulta,
        text="Clientes Cadastrados",
        font=("Arial", 20, "bold"),
        bg=VERMELHO_ESCURO,
        fg=BRANCO
    )
    titulo_consulta.pack(pady=20)

    frame_lista = tk.Frame(
        janela_consulta,
        bg=VERMELHO_ESCURO
    )
    frame_lista.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )

    lista_clientes = tk.Listbox(
        frame_lista,
        bg=BRANCO,
        fg=VERMELHO_ESCURO,
        font=("Arial", 11),
        width=90,
        height=12,
        selectbackground=ROSA,
        selectforeground=BRANCO,
        relief="flat",
        borderwidth=0
    )
    lista_clientes.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar = tk.Scrollbar(
        frame_lista,
        command=lista_clientes.yview,
        bg=ROSA
    )
    scrollbar.pack(
        side="right",
        fill="y"
    )

    lista_clientes.config(
        yscrollcommand=scrollbar.set
    )

    if len(clientes) == 0:
        lista_clientes.insert(
            tk.END,
            "Nenhum cliente cadastrado"
        )
    else:
        for cliente in clientes:
            linha = (
                cliente["nome"] + " | " +
                cliente["telefone"] + " | " +
                cliente["email"] + " | " +
                cliente["endereco"]
            )

            lista_clientes.insert(
                tk.END,
                linha
            )
    botao_fechar = tk.Button(
        janela_consulta,
        text="Fechar",
        command=janela_consulta.destroy,
        bg=ROSA,
        fg=VERMELHO_ESCURO,
        font=("Arial", 11, "bold"),
        width=15,
        height=2,
        relief="flat",
        cursor="hand2"
    )
    botao_fechar.pack(pady=15)


janela = tk.Tk()

janela.title("TechBairro - Cadastro de Clientes")
janela.geometry("600x520")
janela.configure(bg=VERMELHO_ESCURO)
janela.resizable(False, False)

titulo = tk.Label(
    janela,
    text="TechBairro",
    font=("Arial", 26, "bold"),
    bg=VERMELHO_ESCURO,
    fg=BRANCO
)
titulo.pack(pady=(25, 5))

subtitulo = tk.Label(
    janela,
    text="Cadastro de Cliente",
    font=("Arial", 14, "bold"),
    bg=VERMELHO_ESCURO,
    fg=ROSA_CLARO
)
subtitulo.pack(pady=(0, 20))

frame = tk.Frame(
    janela,
    bg=VERMELHO,
    padx=25,
    pady=20
)
frame.pack(
    padx=40,
    fill="x"
)

tk.Label(
    frame,
    text="Nome:",
    font=("Arial", 11, "bold"),
    bg=VERMELHO,
    fg=BRANCO
).grid(
    row=0,
    column=0,
    sticky="w",
    padx=5,
    pady=8
)

entrada_nome = tk.Entry(
    frame,
    width=40,
    font=("Arial", 11),
    bg=BRANCO,
    fg=VERMELHO_ESCURO,
    relief="flat"
)
entrada_nome.grid(
    row=0,
    column=1,
    padx=5,
    pady=8
)

tk.Label(
    frame,
    text="Telefone:",
    font=("Arial", 11, "bold"),
    bg=VERMELHO,
    fg=BRANCO
).grid(
    row=1,
    column=0,
    sticky="w",
    padx=5,
    pady=8
)

entrada_telefone = tk.Entry(
    frame,
    width=40,
    font=("Arial", 11),
    bg=BRANCO,
    fg=VERMELHO_ESCURO,
    relief="flat"
)
entrada_telefone.grid(
    row=1,
    column=1,
    padx=5,
    pady=8
)

tk.Label(
    frame,
    text="E-mail:",
    font=("Arial", 11, "bold"),
    bg=VERMELHO,
    fg=BRANCO
).grid(
    row=2,
    column=0,
    sticky="w",
    padx=5,
    pady=8
)

entrada_email = tk.Entry(
    frame,
    width=40,
    font=("Arial", 11),
    bg=BRANCO,
    fg=VERMELHO_ESCURO,
    relief="flat"
)
entrada_email.grid(
    row=2,
    column=1,
    padx=5,
    pady=8
)

tk.Label(
    frame,
    text="Endereço:",
    font=("Arial", 11, "bold"),
    bg=VERMELHO,
    fg=BRANCO
).grid(
    row=3,
    column=0,
    sticky="w",
    padx=5,
    pady=8
)

entrada_endereco = tk.Entry(
    frame,
    width=40,
    font=("Arial", 11),
    bg=BRANCO,
    fg=VERMELHO_ESCURO,
    relief="flat"
)
entrada_endereco.grid(
    row=3,
    column=1,
    padx=5,
    pady=8
)

frame_botoes = tk.Frame(
    janela,
    bg=VERMELHO_ESCURO
)
frame_botoes.pack(pady=25)

botao_cadastrar = tk.Button(
    frame_botoes,
    text="Cadastrar Cliente",
    command=cadastrar_cliente,
    bg=VERMELHO,
    fg=BRANCO,
    font=("Arial", 11, "bold"),
    width=20,
    height=2,
    relief="flat",
    cursor="hand2"
)
botao_cadastrar.grid(
    row=0,
    column=0,
    padx=8
)

botao_consultar = tk.Button(
    frame_botoes,
    text="Consultar Clientes",
    command=abrir_consulta,
    bg=ROSA,
    fg=VERMELHO_ESCURO,
    font=("Arial", 11, "bold"),
    width=20,
    height=2,
    relief="flat",
    cursor="hand2"
)
botao_consultar.grid(
    row=0,
    column=1,
    padx=8
)

janela.mainloop()