from random import randint
from time import sleep
from colorama import Fore
import colorama
colorama.init(autoreset=True)


while True: 
    bot = randint(0,100)

    chances = 0

    #Jogo enquanto o player tenta acertar
    while True:
        # Rodando o jogo
        if chances == 7:
            print(f"{Fore.RED}Acabaram suas chances! O número era {bot}!")
            break

        user = int(input(f"{Fore.BLUE}Adivinhe o número que eu escolhi: "))

        # Se for menor
        if user < bot:
            print(f"{Fore.YELLOW}Eu escolhi um número maior.")
            chances += 1
            continue

        # Se for maior
        elif user > bot:
            print(f"{Fore.YELLOW}Eu escolhi um número menor.")
            chances += 1
            continue

        # Se acertar
        if user == bot:
            print(f"{Fore.GREEN}Você acertou! Eu escolhi o número {bot}!")
            break

    #Perguntando se quer jogar de novo
    while True:
        again = input(f"{Fore.BLUE}Você quer jogar de novo? [S/N] ").upper()

        if again == "S" or again =="N":
            break

        else:
            continue

    if again == "S":
        print(f"{Fore.BLUE}Pensando em um novo número...")
        sleep(2)
        continue

    elif again == "N":
        print(f"{Fore.BLUE}Até logo!")
        break