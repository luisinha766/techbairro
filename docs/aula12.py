import tkinter as tk

janela = tk.Tk()
janela.title("exemplo de tkinter")
janela.geometry("400x300")

clientes = [
    {"nome": "ana", "telefone: "9999-1111, "e-mail: "ana@gamil.com"}
    {"nome": "bruno", "telefone: "9898-1818, "e-mail: "bruno@gamil.com"}
    {"nome": "carlos", "telefone: "9777-7777, "e-mail: "carlos@gamil.com"}
]

def abrir_janela_teste():
    nova =tk.Toplevel(janela)
    nova.title("janela de teste")
    nova.geometry("250x180")
    tk.Label(nova, text= "ola sou uma janela secundaria.").pack(pady=20)
tk.Button(janela,text="abrir janela de teste", command= abrir_janela_teste).pack(pady=20)

def abrir_lista_teste():
    nova = tk.Toplavel(janela)
    nova.title("janela de teste")
    nova.geometry("250x100")
    tk.label(nova, text-"ola sou uma janela secundaria").pack(pady=20)
    
    lista = tk.Listbox(nova, width=40)
    lista
def mostrar_cliente():
    return
def abrir_lista_com_scroll():
    return

tk.Button(janela,text="1 - toplevel", command= abrir_janela_teste).pack(pady=10)

tk.Button(janela,text="2 - toplevel", command= abrir_janela_teste).pack(pady=10)

tk.Button(janela,text="3 - toplevel", command= abrir_janela_teste).pack(pady=10)

tk.Button(janela,text="4 - toplevel", command= abrir_janela_teste).pack(pady=10)
#anela.mainloop()

import tkinter as tk

janela = tk.Tk()
janela.title("Exemplos de Tkinter")
janela.geometry("400x300")

clientes = [
    {"Nome": "Ana", "Telefone": "9999-1111", "E-mail": "ana@gmail.com"},
    {"Nome": "Bruno", "Telefone": "9898-1818", "E-mail": "Bruno@gmail.com"},
    {"Nome": "Carlos", "Telefone": "9777-7777", "E-mail": "Carlos@gmail.com"}
]


def abrir_janela_teste():
    nova = tk.Toplevel(janela)
    nova.title("Janela de teste")
    nova.geometry("250x100")
    tk.Label(nova, text="Ola! Sou uma janela secundária.").pack(pady=20)

def abrir_lista_teste():
    nova = tk.Toplevel(janela)
    nova.title("Lista de Teste")
    nova.geometry("350x200")

    lista = tk.Listbox(nova, width=40)
    lista.pack(padx=10, pady=10)

    for cliente in clientes:
        texto = f"{cliente['Nome']} - {cliente['Telefone']}"
        lista.insert(tk.END, texto)
   
def mostrar_clientes():
    return  
   
def abrir_lista_com_scroll():
    return  
   
tk.Button(janela,text="1 - Toplevel", command= abrir_janela_teste).pack(pady=10)

tk.Button(janela,text="2 - Listbox", command= abrir_lista_teste).pack(pady=10)

tk.Button(janela,text="3 - For + f-string", command= mostrar_clientes).pack(pady=10)

tk.Button(janela,text="4 - Listbox + Scrollbar", command= abrir_lista_com_scroll).pack(pady=10)

janela.mainloop()
