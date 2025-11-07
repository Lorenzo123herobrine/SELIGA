import random

def jogar():
    print("🎮 Bem-vindo ao Pedra, Papel e Tesoura!")
    opcoes = ["pedra", "papel", "tesoura"]
    
    while True:
        jogador = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower().strip()

        # Condicional de saída
        if jogador == "sair":
            print("👋 Jogo encerrado. Até a próxima!")
            break

        if jogador not in opcoes:
            print("⚠️ Opção inválida, tente novamente.")
            continue

        # Escolha do computador
        computador = random.choice(opcoes)
        print(f"O computador escolheu: {computador}")

        # Condicionais para definir o vencedor
        if jogador == computador:
            print("🤝 Empate!")
        elif (jogador == "pedra" and computador == "tesoura") or \
             (jogador == "papel" and computador == "pedra") or \
             (jogador == "tesoura" and computador == "papel"):
            print("🏆 Você venceu!")
        else:
            print("😅 Você perdeu!")

        print("-" * 30)

# Executa o jogo
jogar()