import os
import time

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

def tocar_som_menu():
    # Emite um bipe sonoro estilo 8-bits no terminal
    print('\a', end='')

def menu_inicial():
    opcoes = ["Novo Jogo", "Carregar", "Créditos"]
    linha_selecionada = 0

    while True:
        limpar_tela()
        print("=" * 65)
        # Título grande customizado "Aventuras de Ekul" em ASCII Art
        print(r"""
    _                   _                       _        _____ _          _ 
   / \   __   __ ___   | |_   _   _  _ __    __| |      | ____| | __  _  | |
  / _ \  \ \ / // _ \  | __| | | | || '__|  / _` |      |  _|   |/ / | | | |
 / ___ \  \ V /|  __/  | |_  | |_| || |    | (_| |      | |___  |   <  | |_| |
/_/   \_\  \_/  \___|   \__|  \__,_||_|     \__,_|      |_____| |_|\_\  \___/ 
        """)
        print("=" * 65)
        print("                      [ EDIÇÃO ANOS 80 ]                       \n")
        
        for i, opcao in enumerate(opcoes):
            if i == linha_selecionada:
                print(f"      >>  {opcao}  <<")
            else:
                print(f"          {opcao}")
        
        print("\n" + "=" * 65)
        print("Controles: [W] Cima | [S] Baixo | [E] Escolher")
        
        comando = input("Ação: ").lower()

        if comando == 'w' and linha_selecionada > 0:
            linha_selecionada -= 1
            tocar_som_menu()
        elif comando == 's' and linha_selecionada < len(opcoes) - 1:
            linha_selecionada += 1
            tocar_som_menu()
        elif comando == 'e':
            tocar_som_menu()
            return linha_selecionada

# ==========================================
# LAÇO PRINCIPAL DO PROGRAMA
# ==========================================
if __name__ == "__main__":
    while True:
        escolha = menu_inicial()
        
        if escolha == 0:
            limpar_tela()
            print("Carregando fitas magnéticas...")
            time.sleep(1)
            print("A fita VHS começa a rodar... Iniciando a investigação de Ekul!\n")
            time.sleep(1)
            
            meu_detetive = Personagem("Ekul")
            meu_jogo = Game()
            meu_jogo.iniciar_mapa()
            meu_jogo.jogar(meu_detetive)
            
        elif escolha == 1:
            limpar_tela()
            print("Aviso: A função de carregar o jogo será implementada no futuro!")
            input("\nPressione ENTER para voltar ao menu...")
            
        elif escolha == 2:
            limpar_tela()
            print("=== CRÉDITOS ===")
            print("Desenvolvedor: Você")
            print("Protagonista: Ekul")
            print("Projeto: Aventuras de Ekul (Estilo Anos 80)")
            input("\nPressione ENTER para voltar ao menu...")
