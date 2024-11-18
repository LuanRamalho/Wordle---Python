import random
from colorama import Fore, Style, init

# Inicializa o colorama para suportar cores no terminal
init(autoreset=True)

# Lista de palavras possíveis (em português)
palavras = [
    "maior", "casar", "verde", "comer", "dente",
    "pular", "lugar", "vezes", "pedra", "vento",
    "carro", "barco", "terra", "folha", "areia",
    "noite", "monte", "campo", "salto", "trigo",
    "nuvem", "sonho", "chave", "forno", "vidro",
    "amigo", "ferro", "cinco", "justo", "grato",
    "certo", "ponto", "festa", "papel", "lápis",
    "troca", "leite", "marca", "reino", "prato",
    "guiar", "longe", "passe", "rever", "torre",
    "união", "pasto", "brisa", "couro", "linha",
    "norte", "sulco", "viver", "porta", "cesto",
    "trena", "caixa", "limpo", "somar", "dessa",
    "baixo", "peixe", "farto", "sorte", "primo",
    "calmo", "velho", "troco", "livro", "morar",
    "banho", "parar", "claro", "faixa", "lapso",
    "feroz", "ouvir", "casco", "chefe", "falar",
    "preto", "fraco", "surdo", "lutar", "prego"
]



# Escolhe uma palavra aleatória da lista
palavra_correta = random.choice(palavras)

def verificar_palavra(chute, palavra_correta):
    resultado = []
    for i, letra in enumerate(chute):
        if letra == palavra_correta[i]:
            resultado.append(Fore.GREEN + letra + Style.RESET_ALL)  # Letra correta e na posição certa
        elif letra in palavra_correta:
            resultado.append(Fore.YELLOW + letra + Style.RESET_ALL)  # Letra correta, mas posição errada
        else:
            resultado.append(Fore.LIGHTBLACK_EX + letra + Style.RESET_ALL)  # Letra incorreta
    return "".join(resultado)

# Função principal do jogo
def jogar_wordle():
    print(Fore.CYAN + "Bem-vindo ao Wordle em Português!" + Style.RESET_ALL)
    print("Você tem 6 tentativas para adivinhar a palavra de 5 letras.")
    print("Dicas:")
    print(f"{Fore.GREEN}Verde{Style.RESET_ALL}: Letra correta na posição certa")
    print(f"{Fore.YELLOW}Amarelo{Style.RESET_ALL}: Letra correta na posição errada")
    print(f"{Fore.LIGHTBLACK_EX}Cinza{Style.RESET_ALL}: Letra incorreta\n")

    tentativas = 6
    for tentativa in range(1, tentativas + 1):
        while True:
            chute = input(f"Tentativa {tentativa}/{tentativas} - Digite uma palavra de 5 letras: ").strip().lower()
            if len(chute) == 5 and chute.isalpha():
                break
            print(Fore.RED + "Entrada inválida! Certifique-se de digitar uma palavra de 5 letras.\n" + Style.RESET_ALL)

        if chute == palavra_correta:
            print(Fore.GREEN + f"Parabéns! Você acertou a palavra: {palavra_correta}!" + Style.RESET_ALL)
            return

        # Mostra o resultado da tentativa
        resultado = verificar_palavra(chute, palavra_correta)
        print(f"Resultado: {resultado}\n")

    print(Fore.RED + f"Você usou todas as tentativas! A palavra correta era: {palavra_correta}." + Style.RESET_ALL)
    input()

# Executa o jogo
if __name__ == "__main__":
    jogar_wordle()
