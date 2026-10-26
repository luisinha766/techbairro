import tkinter as tk

# Importa o messagebox para exibir mensagens e confirmações
from tkinter import messagebox

# NOVO NA AULA 14: importa o módulo do SQLite (já vem com o Python)
import sqlite3

# NOVO NA ATIVIDADE: importa o módulo os
import os

from cliente import Cliente
from banco import GerenciadorClientes
from validacao import ValidadorCliente


# ============================================================
# JANELA PRINCIPAL
# ============================================================

janela = tk.Tk()

janela.title("TechBairro — Cadastro de Cliente")

janela.geometry("480x460")

janela.resizable(False, False)

VERSAO = "3.3.2"


# ============================================================
# OBJETO GERENCIADOR
# ============================================================

# NOVO NA ATIVIDADE: caminho completo do banco
PASTA_DO_PROJETO = os.path.dirname(os.path.abspath(__file__))

CAMINHO_BANCO = os.path.join(
    PASTA_DO_PROJETO,
    "techbairro.db"
)

print(f"Banco em uso: {CAMINHO_BANCO}")

gerenciador = GerenciadorClientes(CAMINHO_BANCO)

validador = ValidadorCliente()


# Guarda o id do cliente que está sendo editado
id_em_edicao = None


# ============================================================
# CABEÇALHO DA INTERFACE
# ============================================================

cabecalho = tk.Frame(
    janela,
    bg="#2c3e50"
)

cabecalho.pack(
    side="top",
    fill="x"
)


tk.Label(
    cabecalho,
    text="Cadastro de Cliente",
    fg="white",
    bg="#2c3e50",
    font=("Arial", 14, "bold"),
    pady=12
).pack()


# ============================================================
# FORMULÁRIO
# ============================================================

form = tk.Frame(janela)

form.pack(
    pady=20
)


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


# ============================================================
# STATUS
# ============================================================

status = tk.Label(
    janela,
    text="Nenhum cliente cadastrado ainda",
    fg="gray",
    wraplength=440,
    justify="left"
)

status.pack(
    pady=(0, 5)
)


contador = tk.Label(
    janela,
    text=f"Clientes cadastrados: {gerenciador.total()}"
)

contador.pack()


# ============================================================
# LIMPAR CAMPOS
# ============================================================

def limpar_campos():

    global id_em_edicao

    for entrada in entradas.values():

        entrada.delete(
            0,
            tk.END
        )

    id_em_edicao = None


# ============================================================
# SALVAR
# ============================================================

def salvar():

    global id_em_edicao

    valores = {
        campo: entradas[campo].get().strip()
        for campo in campos
    }

    cliente = Cliente(
        valores["Nome"],
        valores["Telefone"],
        valores["E-mail"],
        valores["Endereço"]
    )

    # MUDOU NA AULA 21: as regras saíram daqui e foram
    # para o ValidadorCliente (validacao.py).
    # A tela só pergunta e mostra a resposta.
    erro = validador.validar(cliente)

    if erro is not None:

        status.config(
            text=erro,
            fg="red"
        )

        return

    try:

        if id_em_edicao is None:

            gerenciador.adicionar(cliente)

            status.config(
                text=f"Cliente '{cliente.nome}' salvo com sucesso!",
                fg="green"
            )

        else:

            gerenciador.atualizar(
                id_em_edicao,
                cliente
            )

            status.config(
                text=f"Cliente '{cliente.nome}' atualizado com sucesso!",
                fg="green"
            )

    except sqlite3.Error as erro:

        status.config(
            text=f"Erro ao salvar no banco: {erro}",
            fg="red"
        )

        return

    contador.config(
        text=f"Clientes cadastrados: {gerenciador.total()}"
    )

    limpar_campos()


# ============================================================
# CANCELAR
# ============================================================

def cancelar():

    limpar_campos()

    status.config(
        text="Formulário limpo",
        fg="gray"
    )


# ============================================================
# CONSULTA DE CLIENTES
# ============================================================

def abrir_consulta():

    consulta = tk.Toplevel(janela)

    consulta.title(
        "Consulta de Clientes"
    )

    consulta.geometry(
        "500x380"
    )

    consulta.resizable(
        False,
        False
    )


    # ========================================================
    # LISTBOX
    # ========================================================

    lista = tk.Listbox(
        consulta,
        width=65,
        height=12
    )

    lista.pack(
        padx=10,
        pady=10
    )


    # ========================================================
    # BARRA DE ROLAGEM
    # ========================================================

    scrollbar = tk.Scrollbar(
        consulta
    )

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


    # ========================================================
    # ATUALIZAR LISTA
    # ========================================================

    def atualizar_lista():

        lista.delete(
            0,
            tk.END
        )

        try:

            clientes_cadastrados = gerenciador.listar()

        except sqlite3.Error as erro:

            lista.insert(
                tk.END,
                f"Erro ao ler o banco: {erro}"
            )

            return

        if not clientes_cadastrados:

            lista.insert(
                tk.END,
                "Nenhum cliente cadastrado"
            )

            return

        for cliente in clientes_cadastrados:

            lista.insert(
                tk.END,
                cliente.resumo()
            )


    # ========================================================
    # EDITAR CLIENTE
    # ========================================================

    def editar_cliente():

        global id_em_edicao

        selecionado = lista.curselection()

        if not selecionado:

            messagebox.showwarning(
                "Atenção",
                "Selecione um cliente antes de editar."
            )

            return

        indice = selecionado[0]

        cliente = gerenciador.listar()[
            indice
        ]

        id_em_edicao = cliente.id


        # ====================================================
        # COLOCA OS DADOS NO FORMULÁRIO
        # ====================================================

        entradas["Nome"].delete(
            0,
            tk.END
        )

        entradas["Nome"].insert(
            0,
            cliente.nome
        )


        entradas["Telefone"].delete(
            0,
            tk.END
        )

        entradas["Telefone"].insert(
            0,
            cliente.telefone
        )


        entradas["E-mail"].delete(
            0,
            tk.END
        )

        entradas["E-mail"].insert(
            0,
            cliente.email
        )


        entradas["Endereço"].delete(
            0,
            tk.END
        )

        entradas["Endereço"].insert(
            0,
            cliente.endereco
        )


        status.config(
            text=f"Editando cliente: {cliente.nome}",
            fg="blue"
        )

        consulta.destroy()


    # ========================================================
    # EXCLUIR CLIENTE
    # ========================================================

    def excluir_cliente():

        selecionado = lista.curselection()

        if not selecionado:

            messagebox.showwarning(
                "Atenção",
                "Selecione um cliente antes de excluir."
            )

            return

        indice = selecionado[0]

        cliente = gerenciador.listar()[indice]


        # ====================================================
        # CONFIRMAÇÃO
        # ====================================================

        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            f"Tem certeza que deseja excluir o cadastro de "
            f"{cliente.nome}?\n\n"
            f"Essa ação não pode ser desfeita."
        )

        if not confirmar:
            return

        try:

            gerenciador.remover(
                cliente.id
            )

        except sqlite3.Error as erro:

            messagebox.showerror(
                "Erro no banco",
                f"Não foi possível excluir o cliente.\n{erro}"
            )

            return


        atualizar_lista()

        contador.config(
            text=f"Clientes cadastrados: {gerenciador.total()}"
        )

        status.config(
            text=f"Cliente '{cliente.nome}' excluído com sucesso!",
            fg="green"
        )


    # ========================================================
    # BOTÕES DA CONSULTA
    # ========================================================

    botoes_consulta = tk.Frame(
        consulta
    )

    botoes_consulta.pack(
        pady=10
    )


    tk.Button(
        botoes_consulta,
        text="Editar selecionado",
        width=18,
        command=editar_cliente
    ).grid(
        row=0,
        column=0,
        padx=5
    )


    tk.Button(
        botoes_consulta,
        text="Excluir selecionado",
        width=18,
        command=excluir_cliente
    ).grid(
        row=0,
        column=1,
        padx=5
    )


    atualizar_lista()


# ============================================================
# BOTÕES DA JANELA PRINCIPAL
# ============================================================

botoes = tk.Frame(
    janela
)

botoes.pack(
    pady=10
)


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


# ============================================================
# VERSÃO
# ============================================================

tk.Label(
    janela,
    text="v3.3.1",
    fg="gray"
).place(
    relx=0.97,
    rely=0.97,
    anchor="se"
)


# Mantém a aplicação aberta
janela.mainloop()