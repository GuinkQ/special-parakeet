import os
import time
import sys

class Personagem:
    def __init__(self, nome_do_jogador):
        self.nome = nome_do_jogador
        self.coragem = 100
        self.mochila = []
        self.caderno_de_pistas = []

    def investigar(self, objeto):
        print(f"\n> {self.nome} se aproxima e examina: {objeto}...")

    def guardar_na_mochila(self, item):
        self.mochila.append(item)
        print(f"\n> Você guardou [{item}] na sua mochila.")

    def anotar_pista(self, pista):
        self.caderno_de_pistas.append(pista)
        print(f'\n> Nova anotação no caderno: "{pista}"')


class Cenario:
    def __init__(self, nome_local, descricao):
        self.nome_local = nome_local
        self.descricao = descricao
        self.itens_no_local = []
        self.pistas_no_local = []

    def mostrar_cenario(self):
        print(f"\n=== {self.nome_local} ===")
        print(self.descricao)
        
        if self.itens_no_local:
            itens = ", ".join(self.itens_no_local)
            print(f"[!] Você percebe algo jogado aqui: {itens}")


class Game:
    def __init__(self):
        self.locais = [] 

    def iniciar_mapa(self):
        casa = Cenario("Sua Casa", "Seu quarto está bagunçado. Pôsteres de filmes de ficção científica na parede e um Walkman na cama.")
        casa.itens_no_local.extend(["Taco de Beisebol", "Walkman"])

        vizinho_legal = Cenario("Casa do Vizinho Legal", "O Sr. Silva está sempre consertando o rádio na garagem. Ele é gente boa.")
        vizinho_legal.pistas_no_local.append("O Sr. Silva ouviu barulhos estranhos vindo da casa abandonada ontem à noite.")

        mercadinho = Cenario("Mercadinho da Esquina", "Cheiro de chiclete e chão encerado. As prateleiras estão cheias de salgadinhos coloridos.")
        mercadinho.itens_no_local.append("Biscoito Recheado")

        fliperama = Cenario("Fliperama 'Galaxy'", "Luzes neon piscando e sons de jogos de 8-bits. O lugar está cheio de adolescentes.")
        fliperama.pistas_no_local.append("A máquina de Pac-Man tem um mapa estranho desenhado na lateral.")

        casa_abandonada = Cenario("Casa Abandonada", "As janelas estão quebradas e a porta rangendo. O mato está alto. Dá arrepios.")

        vizinho_estranho = Cenario("Casa do Vizinho Estranho", "A casa do Sr. Edgar. As cortinas estão sempre fechadas e o cachorro não para de latir.")

        locadora = Cenario("Locadora de Vídeo 'VHS Magic'", "Paredes cobertas de fitas VHS de terror e ação. O balconista parece saber de tudo.")
        locadora.itens_no_local.append("Lanterna sem pilha")

        self.locais = [casa, vizinho_legal, mercadinho, fliperama, casa_abandonada, vizinho_estranho, locadora]
        
    def jogar(self, heroi):
        local_atual = self.locais[0]
        local_atual.mostrar_cenario()
        
        while True:
            print(f"\n--- {local_atual.nome_local} ---")
            print("O que você quer fazer?")
            print("1. Olhar ao redor (Procurar itens)")
            print("2. Investigar (Procurar pistas)")
            print("3. Ver Mochila e Caderno de Pistas")
            print("4. Ir para outro local do bairro")
            print("5. Voltar ao Menu Principal")
            
            escolha = input("Digite o número da sua escolha: ")
            
            if escolha == "1":
                if local_atual.itens_no_local:
                    item = local_atual.itens_no_local.pop(0)
                    heroi.guardar_na_mochila(item)
                else:
                    print("\n> Não há mais nada de útil para pegar aqui.")
            elif escolha == "2":
                if local_atual.pistas_no_local:
                    pista = local_atual.pistas_no_local.pop(0)
                    heroi.anotar_pista(pista)
                else:
                    print("\n> Você não encontra nada de suspeito por aqui.")
            elif escolha == "3":
                print(f"\n--- Mochila ---: {heroi.mochila}")
                print(f"--- Caderno ---: {heroi.caderno_de_pistas}")
                print(f"--- Coragem ---: {heroi.coragem}%")
            elif escolha == "4":
                print("\nPara onde você quer ir?")
                for i, local in enumerate(self.locais):
                    print(f"{i + 1}. {local.nome_local}")
                
                destino = input("Digite o número do destino: ")
                
                if destino.isdigit() and 1 <= int(destino) <= len(self.locais):
                    local_atual = self.locais[int(destino) - 1]
                    print(f"\n> Você caminhou até: {local_atual.nome_local}")
                    local_atual.mostrar_cenario()
                else:
                    print("\n> Destino inválido.")
            elif escolha == "5":
                print("\nVoltando ao menu principal...")
                break
            else:
                print("\n> Opção inválida. Tente novamente com um número de 1 a 5.")


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def tocar_bipe():
    # Emite um bipe de áudio simulando estilo 8-bits no terminal
    print('\a', end='', flush=True)

# Função especial para ler as setas do teclado ao vivo (como um evento KeyDown)
def ler_tecla():
    if os.name == 'nt':  # Sistema Windows
        import msvcrt
        tecla = msvcrt.getch()
        if tecla == b'\xe0':  # Prefixo das setas no Windows
            tecla = msvcrt.getch()
            if tecla == b'H': return 'cima'
            if tecla == b'P': return 'baixo'
        elif tecla in (b'\r', b'\n'):
            return 'enter'
        return tecla.decode('utf-8', 'ignore').lower()
    else:  # Sistemas baseados em Linux/Mac (como o ambiente do GitHub/Replit)
        import tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            if ch == '\x1b':  # Prefixo da tecla ESC e das setas
                ch += sys.stdin.read(2)
                if ch == '\x1b[A': return 'cima'
                if ch == '\x1b[B': return 'baixo'
            elif ch in ('\r', '\n'):
                return 'enter'
            return ch.lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def menu_inicial():
    opcoes = ["Novo Jogo", "Carregar", "Créditos"]
    linha_selecionada = 0

    while True:
        limpar_tela()
        print("=" * 75)
        # Arte ASCII corrigida para BAIRRO MISTERIOSO
        print(r"""
   ____        _                     __  __ _     _            _                 
  |  _ \      (_)                   |  \/  (_)   | |          (_)                
  | |_) | __ _ _ _ __ _ __ ___      | \  / |_ ___| |_ ___ _ __ _  ___  ___  ___  
  |  _ < / _` | | '__| '__/ _ \     | |\/| | / __| __/ _ \ '__| |/ _ \/ __|/ _ \ 
  | |_) | (_| | | |  | | | (_) |    | |  | | \__ \ ||  __/ |  | | (_) \__ \ (_) |
  |____/ \__,_|_|_|  |_|  \___/     |_|  |_|_|___/\__\___|_|  |_|\___/|___/\___/ 
        """)
        print("                 [ EDIÇÃO DE INVESTIGAÇÃO ANOS 80 ]                 \n")
        
        # Renderiza as opções e coloca a setinha '
