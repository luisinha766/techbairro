import tkinter as tk

janela = tk.Tk()
janela.title("TechBairro - Cadastro de Cliente")
janela.geometry("500x350")
topo = tk.Frame(janela, bg="#54fff1")
topo.pack(side="top", fill="x")
tk.Label(
    topo,
    text="Cadastro de cliente",
    fg="white",
    bg="#14c0cc",
    pady=10
    
).pack()
form = tk.Frame(janela)
form.pack(pady=20)
campos = ["Nome", "Telefone", "E-mail", "Endereço"]
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

clientes = []
def salvar_nome():
    nome = entradas["Nome"].get().strip()
    telefone = entradas["Telefone"].get()
    email = entradas["E-mail"].get()
    endereco = entradas["Endereço"].get()
    if nome == "":
        status.config(text="Digite o nome!")
    else:
        clientes.append({
            "Nome": nome,
            "Telefone": telefone,
            "E-mail": email,
            "Endereço": endereco
        })

        status.config(text="Cliente salvo!")
        contador.config(
            text=f"Clientes cadastrados: {len(clientes)}"
        )

        entradas["Nome"].delete(0, tk.END)
        entradas["Telefone"].delete(0, tk.END)
        entradas["E-mail"].delete(0, tk.END)
        entradas["Endereço"].delete(0, tk.END)
def cancelar():
    entradas["Nome"].delete(0, tk.END)
    entradas["Telefone"].delete(0, tk.END)
    entradas["E-mail"].delete(0, tk.END)
    entradas["Endereço"].delete(0, tk.END)
    status.config(text="")
status = tk.Label(form, text="")
status.grid(row=5, column=0, columnspan=2, pady=5)
contador = tk.Label(
    form,
    text="Clientes cadastrados: 0"
)
contador.grid(row=6, column=0, columnspan=2, pady=5)
botao_salvar = tk.Button(
    form,
    text="Salvar",
    command=salvar_nome
)
botao_salvar.grid(row=7, column=0, pady=10)
botao_cancelar = tk.Button(
    form,
    text="Cancelar",
    command=cancelar
)
botao_cancelar.grid(row=7, column=1, pady=10)

janela.mainloop()