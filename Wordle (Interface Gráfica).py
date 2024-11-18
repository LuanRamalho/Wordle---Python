import random
import tkinter as tk
from tkinter import messagebox

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

class WordleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordle em Português")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.tentativas_restantes = 6
        self.palavra_correta = palavra_correta
        self.palavras_digitadas = []
        
        # Interface
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Wordle em Português", font=("Helvetica", 20, "bold"), fg="blue").pack(pady=10)
        tk.Label(self.root, text="Descubra a palavra secreta em 6 tentativas!", font=("Helvetica", 12), fg="black").pack()

        # Área das tentativas
        self.canvas = tk.Canvas(self.root, width=300, height=360, bg="white")
        self.canvas.pack(pady=10)

        # Entrada de texto
        self.input_var = tk.StringVar()
        self.input_entry = tk.Entry(self.root, textvariable=self.input_var, font=("Helvetica", 14), justify="center")
        self.input_entry.pack(pady=10)
        self.input_entry.focus()

        # Botão de enviar
        self.submit_button = tk.Button(self.root, text="Enviar", command=self.enviar_tentativa, font=("Helvetica", 14), bg="green", fg="white")
        self.submit_button.pack(pady=5)

        # Status do jogo
        self.status_label = tk.Label(self.root, text=f"Tentativas restantes: {self.tentativas_restantes}", font=("Helvetica", 12), fg="black")
        self.status_label.pack(pady=5)

    def desenhar_tentativa(self, tentativa, cores):
        y = len(self.palavras_digitadas) * 60 + 10
        for i, letra in enumerate(tentativa):
            x = i * 60 + 10
            self.canvas.create_rectangle(x, y, x + 50, y + 50, fill=cores[i], outline="black")
            self.canvas.create_text(x + 25, y + 25, text=letra.upper(), font=("Helvetica", 20, "bold"))

    def enviar_tentativa(self):
        chute = self.input_var.get().strip().lower()
        self.input_var.set("")

        # Valida a entrada
        if len(chute) != 5 or not chute.isalpha():
            messagebox.showerror("Erro", "Por favor, insira uma palavra válida de 5 letras.")
            return

        if chute in self.palavras_digitadas:
            messagebox.showwarning("Aviso", "Você já tentou essa palavra.")
            return

        self.palavras_digitadas.append(chute)
        cores = self.verificar_palavra(chute)

        # Atualiza a interface
        self.desenhar_tentativa(chute, cores)
        self.tentativas_restantes -= 1
        self.status_label.config(text=f"Tentativas restantes: {self.tentativas_restantes}")

        # Verifica se o jogo acabou
        if chute == self.palavra_correta:
            messagebox.showinfo("Parabéns!", f"Você acertou a palavra: {self.palavra_correta.upper()}!")
            self.root.quit()
        elif self.tentativas_restantes == 0:
            messagebox.showinfo("Fim de jogo", f"Você perdeu! A palavra correta era: {self.palavra_correta.upper()}.")
            self.root.quit()

    def verificar_palavra(self, chute):
        cores = []
        for i, letra in enumerate(chute):
            if letra == self.palavra_correta[i]:
                cores.append("green")  # Letra correta e posição correta
            elif letra in self.palavra_correta:
                cores.append("yellow")  # Letra correta, mas posição errada
            else:
                cores.append("gray")  # Letra incorreta
        return cores

# Executa o jogo
if __name__ == "__main__":
    root = tk.Tk()
    app = WordleApp(root)
    root.mainloop()
