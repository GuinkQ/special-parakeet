class Personagem:
    # O método __init__ funciona como o Construtor para inicializar os atributos
    def __init__(self, nome_do_jogador):
        self.nome = nome_do_jogador
        self.coragem = 100
        self.mochila = []
        self.caderno_de_pistas = []

    # Método para o herói investigar algo no cenário
    def investigar(self, objeto):
        print(f"\n> {self.nome} se aproxima e examina: {objeto}...")

    # Método para guardar itens ou pistas
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

    # Método para o jogo exibir o que há na tela
    def mostrar_cenario(self):
        print(f"\n=== {self.nome_local} ===")
        print(self.descricao)
        
        if self.itens_no_local:
            # Junta os itens da lista em um texto
            itens = ", ".join(self.itens_no_local)
            print(f"[!] Você percebe algo jogado aqui: {itens}")


class Game:
    def __init__(self):
        self.locais = [] # Lista que guardará todo o mapa

    def iniciar_mapa(self):
        # 1. Sua Casa
        casa = Cenario("Sua Casa", "Seu quarto está bagunçado. Pôsteres de filmes de ficção científica na parede e um Walkman na cama.")
        casa.itens_no_local.extend(["Taco de Beisebol", "Walkman"])

        # 2. Casa do Vizinho Legal
        vizinho_legal = Cenario("Casa do Vizinho Legal", "O Sr. Silva está sempre consertando o rádio na garagem. Ele é gente boa.")
        vizinho_legal.pistas_no_local.append("O Sr. Silva ouviu barulhos estranhos vindo da casa abandonada ontem à noite.")

        # 3. Mercadinho
        mercadinho = Cenario("Mercadinho da Esquina", "Cheiro de chiclete e chão encerado. As prateleiras estão cheias de salgadinhos coloridos.")
        mercadinho.itens_no_local.append("Biscoito Recheado")

        # 4. Fliperama
        fliperama = Cenario("Fliperama 'Galaxy'", "Luzes neon piscando e sons de jogos de 8-bits. O lugar está cheio de adolescentes.")
        fliperama.pistas_no_local.append("A máquina de Pac-Man tem um mapa estranho desenhado na lateral.")

        # 5. Casa Abandonada
        casa_abandonada = Cenario("Casa Abandonada", "As janelas estão quebradas e a porta rangendo. O mato está alto. Dá arrepios.")

        # 6. Casa do Vizinho Estranho
        vizinho_estranho = Cenario("Casa do Vizinho Estranho", "A casa do Sr. Edgar. As cortinas estão sempre fechadas e o cachorro não para de latir.")

        # 7. Locadora de Vídeo
        locadora = Cenario("Locadora de Vídeo 'VHS Magic'", "Paredes cobertas de fitas VHS de terror e ação. O balconista parece saber de tudo.")
        locadora.itens_no_local.append("Lanterna sem pilha")

        # Guardando todos os cenários na nossa lista do mapa
        self.locais = [casa, vizinho_legal, mercadinho, fliperama, casa_abandonada, vizinho_estranho, locadora]
        
        print("Mapa do bairro carregado com sucesso! Os anos 80 te esperam.")

    def jogar(self, heroi):
        # O herói começa no primeiro local da lista (Sua Casa)
        local_atual = self.locais[0]
        local_atual.mostrar_cenario()
        
        # Este é o Game Loop. O jogo continua rodando enquanto for "True"
        while True:
            print(f"\n--- {local_atual.nome_local} ---")
            print("O que você quer fazer?")
            print("1. Olhar ao redor (Procurar itens)")
            print("2. Investigar (Procurar pistas)")
            print("3. Ver Mochila e Caderno de Pistas")
            print("4. Ir para outro local do bairro")
            print("5. Sair do jogo")
            
            escolha = input("Digite o número da sua escolha: ")
            
            # Estruturas condicionais para processar a ação do jogador
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
                # Mostra o mapa completo com números
                for i, local in enumerate(self.locais):
                    print(f"{i + 1}. {local.nome_local}")
                
                destino = input("Digite o número do destino: ")
                
                # Valida se o jogador digitou um número válido do mapa
                if destino.isdigit() and 1 <= int(destino) <= len(self.locais):
                    local_atual = self.locais[int(destino) - 1]
                    print(f"\n> Você caminhou até: {local_atual.nome_local}")
                    local_atual.mostrar_cenario()
                else:
                    print("\n> Destino inválido.")
                    
            elif escolha == "5":
                print("\nSaindo do jogo... Até mais, detetive Ekul!")
                break # Quebra o laço de repetição e encerra o jogo
                
            else:
                print("\n> Opção inválida. Tente novamente com um número de 1 a 5.")


# ==========================================
# INICIALIZAÇÃO DO JOGO
# ==========================================

# 1. Cria o herói Ekul
meu_detetive = Personagem("Ekul")

# 2. Cria o jogo e carrega o mapa
meu_jogo = Game()
meu_jogo.iniciar_mapa()

# 3. Dá o arranque no Game Loop
meu_jogo.jogar(meu_detetive)
