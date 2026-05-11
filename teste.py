# # def funsimple(a,b):
# #     return a + b
# # print(funsimple(10,24))


# # def nota(nota):
# #     return "aprovado" if nota >= 7 else "reprovado"
# # print(nota(4))


# # def lerdados():
# #     nome = int(input("qual seu nome: "))
# #     idade = int(input("qual sua idade: "))
# #     return (nome,idade)




# # def processardados():
# #     return f"ola seu nome é {dados[0]}, voc~e é menor de idade " if dados[1] >= 18 else f"ola {dados[0]}, voce é menor de idade"



# # def somar(a, b):
# #     return a + b

# # def subtrair(a, b):
# #     return a - b

# # def multiplicar(a, b):
# #     return a * b

# # def dividir(a, b):
# #     if b == 0:
# #         return "amigão não pode por zero"
# #     return a / b


# # def calculadora():
# #     print("welcome calculator")
# #     print("1 somar")
# #     print("2 subtrair")
# #     print("3 multiplicar")
# #     print("4 dividir")

# #     opcao = input("Escolha uma opção: ")

# #     n1 = float(input("digite o primeiro número: "))
# #     n2 = float(input("digite o segundo número: "))
    
# #     if opcao != "1,2,3,4":
# #         print("escolha uma das opções")

# #     elif opcao == "1":
# #         print("resultado", somar(n1, n2))
# #     elif opcao == "2":
# #         print("resultado", subtrair(n1, n2))
# #     elif opcao == "3":
# #         print("resultado", multiplicar(n1, n2))
# #     elif opcao == "4":
# #         print("resultado", dividir(n1, n2))
# #     else:
# #         print("operace invalide")


# # calculadora()



# # def valnome(nome,idade,senha):
# #     if nome.strip() == "" or idade <= 0 or len(senha.strip())< 6:
# #         return False
# #     return True


# # print(valnome("jorge", 24,"1212"))

# # def validade(idade):
# #     if idade <= 0:
# #         return "pode n man"
    
# # def valsenha(senha):
# #     if len(senha) < 8:
# #         return "pode n man"
    



# # def mrvalidation():
    




# usuarios = []

# while True:
#     nome = input("Digite o nome: ")
#     idade = int(input("Digite a idade: "))
#     email = input("Digite o email: ")

#     usuarios.append({
#         "nome": nome,
#         "idade": idade,
#         "email": email
#     })

# #     continuar = input("Quer adicionar outro usuário? (s/n): ")
# #     if continuar.lower() != "s":
# #         break

# # print("\nLista de usuários:")
# # for usuario in usuarios:
# #     print(usuario)



# usuarios = []

# while True:
#     print("\n=== MENU ===")
#     print("1 - Cadastrar usuário")
#     print("2 - Listar usuários")
#     print("3 - Sair")

#     opcao = input("Escolha uma opção: ")

#     if opcao == "1":
#         nome = input("Nome: ")
#         idade = int(input("Idade: "))
#         email = input("Email: ")

#         usuarios.append({
#             "nome": nome,
#             "idade": idade,
#             "email": email
#         })

#         print("Usuário cadastrado com sucesso!")

#     elif opcao == "2":
#         if len(usuarios) == 0:
#             print("Nenhum usuário cadastrado.")
#         else:
#             print("\n=== Usuários cadastrados ===")
#             for i, usuario in enumerate(usuarios, start=1):
#                 print(f"{i}. Nome: {usuario['nome']}, Idade: {usuario['idade']}, Email: {usuario['email']}")

#     elif opcao == "3":
#         print("Saindo...")
#         break

#     else:
#         print("Opção inválida!")



# print(texto.split(" "))
# print(" ".join(texto.split(" ")))

# q = "upper"
# j = q.upper()
# print(q)

# print(texto.lower())
# print(texto.upper())
# print(texto.strip())
# print(len(texto))
# print(len(texto.split(" ")))
# print(len(texto.replace(" ","")))



# texto =input("digite um texto: ").strip()

# print(texto)

# if len(texto) < 8:
#     print("senha curta de mais")

# print(texto.lower())
# print(texto.isalpha())
# print(len(texto))
# print((texto.split(" ")))
# print(texto.replace("gande","peqe"))
# print(texto)

# if "macaco" in texto:
#     print("no puede macaco")



def cifra_cesar(texto, modo):
   alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
   resultado = ''
 
   texto = texto.upper()
   for letra in texto:
       if letra in alfabeto:
           posicao = alfabeto.find(letra)
           if modo == 'E':
               nova_posicao = (posicao + 3)
           elif modo == 'D':
               nova_posicao = (posicao - 3)
           resultado += alfabeto[nova_posicao]
       else:
           
           resultado += letra
   return resultado
texto = input("Digite a mensagem: ")
 
modo = input("Escolha 'E' para encriptar ou 'D' para decriptar: ").upper()
resultado = cifra_cesar(texto, modo)
print(f"Resultado: {resultado}")
 