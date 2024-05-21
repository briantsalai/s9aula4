import random

def adivinhar():
  print("Pense em um númrero entre 1 e 100")
  print("Vou tentar adivinhar")

palpite1 = 1
palpite2 = 100
repetidor = False

while not repetidor:
 guess = random.randint(palpite1, palpite2)
 print("O número que você pensou é", guess, "?")

 resposta = input("Estou certo?: ")
 if resposta == "sim":
  print("Eu sabia!")
  repetidor = True
 elif resposta == "maior":
   palpite1 = guess + 1
 elif resposta == "menor":
  palpite2 = guess - 1
 else:
  print("Desculpe, não entendi sua resposta.")

adivinhar()