

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
 
