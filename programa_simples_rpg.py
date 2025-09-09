import random
import time

forca_voce = random.randint(1, 20)
vida_voce = random.randint(1, 20)
defesa_voce = random.randint(1, 20)

forca_mago = 10
vida_mago = 10
defesa_mago = 15

forca_guerreiro = 10
vida_guerreiro = 10
defesa_guerreiro = 15

forca_ladrao = 20
vida_ladrao = 10
defesa_ladrao = 5

nome_voce = ""

while True:
    print("\nEscolha uma das opçoes abaixo: ")
    print("1-Criar personagem")
    print("2-Batalhar")
    print("3-Sair")
    
    escolha_menu = input("Escolha uma das opções acima: ")

    if escolha_menu == "1":

        nome_voce = input("Qual o nome do seu personagem?: ")
        print(f"\nOlá, {nome_voce}! Seus status são:")
        print(f"Força: 💪 {forca_voce} 💪")
        print(f"Vida: 💚 {vida_voce} 💚")
        print(f"Defesa: 🛡️ {defesa_voce} 🛡️")
        print("\nAgora, escolha a opção 2 para lutar!")
        
    elif escolha_menu == "2":
        if not nome_voce:
            print("\nVocê precisa criar um personagem primeiro (opção 1)!")
            continue  
            
        print("\n Escolha um oponente abaixo: ")
        print("1-Mago")
        print("2-Guerreiro")
        print("3-Ladrão")
        
        escolha_oponente = input("Escolha seu oponente: ")

        vida_atual_voce = vida_voce
        
        nome_oponente = ""
        vida_atual_oponente = 0
        forca_oponente = 0
        defesa_oponente = 0

        if escolha_oponente == "1":
            nome_oponente = "Mago"
            vida_atual_oponente = vida_mago
            forca_oponente = forca_mago
            defesa_oponente = defesa_mago
        elif escolha_oponente == "2":
            nome_oponente = "Guerreiro"
            vida_atual_oponente = vida_guerreiro
            forca_oponente = forca_guerreiro
            defesa_oponente = defesa_guerreiro
        elif escolha_oponente == "3":
            nome_oponente = "Ladrão"
            vida_atual_oponente = vida_ladrao
            forca_oponente = forca_ladrao
            defesa_oponente = defesa_ladrao
        else:
            print("Opção inválida.")
            continue 

        print(f"\n INÍCIO DA BATALHA: {nome_voce} vs {nome_oponente} ")
        time.sleep(1)

        while vida_atual_voce > 0 and vida_atual_oponente > 0:
            dano_bruto_voce = forca_voce - defesa_oponente
            
            if dano_bruto_voce < 0:
                dano_voce = 0
            else:
                dano_voce = dano_bruto_voce
            
            vida_atual_oponente = vida_atual_oponente - dano_voce
            print(f"\nVocê atacou! Causou {dano_voce} de dano.")
            print(f"Vida do {nome_oponente}: {vida_atual_oponente}")
            time.sleep(1)
            
            if vida_atual_oponente <= 0:
                print(f"Você venceu o {nome_oponente}!")
                break
            dano_bruto_oponente = forca_oponente - defesa_voce
            
            if dano_bruto_oponente < 0:
                dano_oponente = 0
            else:
                dano_oponente = dano_bruto_oponente
                
            vida_atual_voce = vida_atual_voce - dano_oponente
            print(f"O {nome_oponente} atacou! Causou {dano_oponente} de dano a você.")
            print(f"Sua vida: {vida_atual_voce}")
            time.sleep(1)

            if vida_atual_voce <= 0:
                print(f"Você foi derrotado pelo {nome_oponente}.")
                break
    
    elif escolha_menu == "3":
        print("Obrigado por jogar! Até a próxima.")
        break 

    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")