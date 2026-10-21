
import tkinter as tk
from tkinter import messagebox

class Cliente:

    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def resumo(self):
        return f"{self.nome} - {self.telefone} - {self.email}"
class GerenciadorClientes:

    def __init__(self):
        self.clientes = []
        self.clientes_removidos = []

    # CREATE
    def adicionar(self, cliente):
        self.clientes.append(cliente)

    # READ
    def listar(self):
        return self.clientes

    # UPDATE
    def atualizar(self, indice, novo_cliente):

        if 0 <= indice < len(self.clientes):
            self.clientes[indice] = novo_cliente
            return True

        return False

    # DELETE
    def remover(self, indice):

        if 0 <= indice < len(self.clientes):

            cliente = self.clientes[indice]

            # Desafio extra: guarda o cliente removido
            self.clientes_removidos.append(cliente)

            self.clientes.pop(indice)

            return True

        return False


# ============================================================
# CONFIGURAÇÃO DA JANELA
# ============================================================

janela = tk.Tk()

janela.title("TechBairro - Cadastro de Clientes")
janela.geometry("550x550")
janela.resizable(False, False)

gerenciador = GerenciadorClientes()

indice_em_edicao = None


# ============================================================
# FORMULÁRIO
# ============================================================

tk.Label(janela, text="Nome:").pack(pady=(15, 3))

entrada_nome = tk.Entry(janela, width=50)
entrada_nome.pack()


tk.Label(janela, text="Telefone:").pack(pady=(8, 3))

entrada_telefone = tk.Entry(janela, width=50)
entrada_telefone.pack()


tk.Label(janela, text="E-mail:").pack(pady=(8, 3))

entrada_email = tk.Entry(janela, width=50)
entrada_email.pack()


tk.Label(janela, text="Endereço:").pack(pady=(8, 3))

entrada_endereco = tk.Entry(janela, width=50)
entrada_endereco.pack()


# ============================================================
# LISTA DE CLIENTES
# ============================================================

tk.Label(
    janela,
    text="Clientes cadastrados:"
).pack(pady=(15, 5))

lista_clientes = tk.Listbox(
    janela,
    width=65,
    height=10
)

lista_clientes.pack()


# ============================================================
# ATUALIZAR LISTA
# ============================================================

def atualizar_lista():

    lista_clientes.delete(0, tk.END)

    for cliente in gerenciador.listar():
        lista_clientes.insert(
            tk.END,
            cliente.resumo()
        )


# ============================================================
# LIMPAR FORMULÁRIO
# ============================================================

def limpar_formulario():

    entrada_nome.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_endereco.delete(0, tk.END)


# ============================================================
# SALVAR
# ============================================================

def salvar():

    global indice_em_edicao

    nome = entrada_nome.get().strip()
    telefone = entrada_telefone.get().strip()
    email = entrada_email.get().strip()
    endereco = entrada_endereco.get().strip()

    # Validação dos campos obrigatórios
    if nome == "" or telefone == "" or email == "" or endereco == "":
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos."
        )
        return

    novo_cliente = Cliente(
        nome,
        telefone,
        email,
        endereco
    )

    # CADASTRAR
    if indice_em_edicao is None:

        gerenciador.adicionar(novo_cliente)

        messagebox.showinfo(
            "Sucesso",
            "Cliente cadastrado!"
        )

    # ATUALIZAR
    else:

        gerenciador.atualizar(
            indice_em_edicao,
            novo_cliente
        )

        messagebox.showinfo(
            "Sucesso",
            "Cliente atualizado!"
        )

        indice_em_edicao = None

    atualizar_lista()
    limpar_formulario()


# ============================================================
# EDITAR SELECIONADO
# ============================================================

def editar():

    global indice_em_edicao

    selecionado = lista_clientes.curselection()

    if not selecionado:

        messagebox.showwarning(
            "Atenção",
            "Selecione um cliente para editar."
        )

        return

    indice_em_edicao = selecionado[0]

    cliente = gerenciador.listar()[indice_em_edicao]

    entrada_nome.delete(0, tk.END)
    entrada_nome.insert(0, cliente.nome)

    entrada_telefone.delete(0, tk.END)
    entrada_telefone.insert(0, cliente.telefone)

    entrada_email.delete(0, tk.END)
    entrada_email.insert(0, cliente.email)

    entrada_endereco.delete(0, tk.END)
    entrada_endereco.insert(0, cliente.endereco)


# ============================================================
# EXCLUIR SELECIONADO
# ============================================================

def excluir():

    selecionado = lista_clientes.curselection()

    if not selecionado:

        messagebox.showwarning(
            "Atenção",
            "Selecione um cliente para excluir."
        )

        return

    indice = selecionado[0]

    cliente = gerenciador.listar()[indice]

    confirmar = messagebox.askyesno(
        "Confirmar exclusão",
        f"Deseja realmente excluir o cliente:\n\n"
        f"{cliente.nome}?"
    )

    if confirmar:

        gerenciador.remover(indice)

        atualizar_lista()
        limpar_formulario()

        messagebox.showinfo(
            "Sucesso",
            "Cliente excluído!"
        )


frame_botoes = tk.Frame(janela)

frame_botoes.pack(pady=20)


tk.Button(
    frame_botoes,
    text="Salvar",
    width=15,
    command=salvar
).grid(row=0, column=0, padx=5)


tk.Button(
    frame_botoes,
    text="Editar selecionado",
    width=18,
    command=editar
).grid(row=0, column=1, padx=5)


tk.Button(
    frame_botoes,
    text="Excluir selecionado",
    width=18,
    command=excluir
).grid(row=1, column=0, columnspan=2, pady=10)


janela.mainloop()