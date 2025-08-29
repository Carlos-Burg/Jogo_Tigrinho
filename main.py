import os 
import random 
import time

def limpa_tela():
    os.system('cls')

def rodada(saldo): #f

    cartas = ["🐯","🎉","💰","💎","🎁","🔔"] #cartas do jogo

    ganhos = {"🐯": 10,"💎": 8,"💰": 5,"🎁": 3, "🔔": 2,"🎉": 1,}

    while True:
        try: 
            vlr_aposta = float(input("Digite o valor da aposta: ")) 
        except ValueError: #verifica se o valor digitado não é nulo
            print("\nDigite um número válido!\n")
            continue

        if vlr_aposta > saldo: #verifica se o valor da aposta é válido
            print(f"\nSALDO: {saldo:.2f}")
            print("Saldo Insuficiente !\n")
        elif vlr_aposta <= 0:
            print(f"\nVALOR: {vlr_aposta:.2f}")
            print("Digite um valor válido !\n")
        else:
            saldo -= vlr_aposta
            break

    limpa_tela() #limpa o terminal

    print("+===============+") #informa o saldo e roda a roleta
    print(f"|SALDO: R${saldo:.2f}  |")
    print("+===============+")
    input("\nDigite enter para rodar: ") 

    # Define chance de vitória
    chance_vitoria = 0.2  # 20% padrão
    if saldo < 10:
        chance_vitoria = 0.3  # 30% se saldo baixo

    # Sorteio com chance de vitória
    if random.random() < chance_vitoria:
        simbolo = random.choice(cartas)
        tentativa = [simbolo, simbolo, simbolo]
    else:
        tentativa = [random.choice(cartas) for _ in range(3)]

    for i in range(3): #"roda" a roleta
        print("\nRodando...", end="\r")
        time.sleep(0.5)

    ganho = 0

    if tentativa[0] == tentativa[1] == tentativa[2]: #verifica se o usuário ganhou
        simbolo = tentativa[0]
        ganho = vlr_aposta * ganhos[simbolo]
        saldo += ganho

    limpa_tela()

    print("\n") #retorna o resultado ao usuário
    print("+==============+")
    print(f"|SALDO: R${saldo:.2f}|")
    print("+==============+")
    print("\n+===================+") 
    print("|     RESULTADO     |")
    print("+===================+")
    print("|", "  -  ".join(tentativa), "|")
    print("+===================+")

    if ganho > 0: #verifica se o usuário ganhou
        print(f"\n🎉 PARABÉNS! Você ganhou R${ganho:.2f}!")
    else:
        print("\nNão foi dessa vez...")

    return saldo

#boas vindas
print("+=============================================+")
print("| 🐯💰 BEM - VINDO AO JOGO DO TIGRINHO ! 🐯💰 |")
print("+=============================================+")

#deposito do saldo
saldo = float(input("\nDeposite o saldo: R$ "))

while True: #verifica se o usuário deseja jogar novamente ou sair

    saldo = rodada(saldo) #saldo retorna da função
 
    if saldo <= 0: #verifica se o saldo é menor ou igual
        print("\nVocê ficou sem saldo! Fim de jogo!") 
        break

    jogar_novamente = input("\nJogar novamente (s/n): ").lower()

    if jogar_novamente == "n":
        limpa_tela()
        print("+=============================+")
        print("| 🐯💰  ATÉ A PRÓXIMA !  🐯💰 |")
        print("+=============================+")
        break