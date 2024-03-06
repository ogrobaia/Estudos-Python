## Criando Janelas para inserir dados ##
# import tkinter

# # Criando janela
# janela = tkinter.tk()
# janela.geometry("500x300")


# # Criar função para o botao


# def clique():
#     print("Fazer Login")


# # Criar uma caixa para o usuario escrever
# texto = tkinter.Label(text="Fazer Login")
# texto.pack(padx=10, pady=10)

# # Criando botão
# botao = tkinter.Button(janela, text="Login", command=clique)
# botao.pack(padx=10, pady=10)

# # Manter a janela aberta
# janela.mainloop()


import customtkinter

# passando parametros para o customtkinter ( ESTILIZANDO A JANELA )
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


# criando janela
janela = customtkinter.CTk()
janela.geometry("500x300")

# Criando clique


def clique():
    print("Fazer Login")


# Criar uma caixa para o usuario escrever
texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

# Entrada de dados
email = customtkinter.CTkEntry(janela, placeholder_text="Sei email")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha.pack(padx=10, pady=10)

# Lembrando a senha e usuario inseridas na janela
checkbox = customtkinter.CTkCheckBox(janela, text="lembrar login")
checkbox.pack(padx=10, pady=10)

# criando botão
botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)


janela.mainloop()
