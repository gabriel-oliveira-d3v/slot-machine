import random 
import time 

figuras = ["💎","🔔","7"]

jogo = ""

nome = input("nome do apostador: ")
valor = float(input("valor da aposta R$: "))

input("pressione Enter para Iniciar...")

print ("Suas apostas: ", end="")

for i in range(3):
    #gera um numero aleatorio entre 0 e 2 
    num = random.randint(0, 2)
    print(figuras[num], end="", flush=True)
    time.sleep(1)
    jogo = jogo + figuras[num]

print()

if jogo[0] == jogo[1] and jogo[0] == jogo[2]:
    premio = valor * 3
    print(f"parabéns {nome}! Você ganhou R$: {premio:.2f} \\(^o^)/")
elif jogo[0] == jogo[1] or jogo[0] == jogo[2] or jogo[1] == jogo[2]:
    premio = valor * 1.5 # exemplo: premio menor para um par
    print(f"Quase! Você ganhou R$: {premio:.2f} (um par)")
else:
    print(f"Que pena, {nome}. você perdeu R$: {valor:.2f} (︶︹︶)")
