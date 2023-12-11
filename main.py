from random import randint, shuffle, uniform
import pygame
from typing import List, Tuple, Any

from gui.gui import InterfaceDrawer
from data_structure.graph import GrafoSimples


def process_event_bus():
    """Função que processa a fila de eventos do PyGame. Necessária
    Para fechar o programa normalmente."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


def get_player_positions() -> List[Tuple[float, float]]:
    """Função temporária que retorna um exemplo de posicionamento para os jogadores."""
    positions = [(0.0, 0.0),
                 (1.0, -2.0), (1.0, -1.0), (1.0, 1.0), (1.0, 2.0),
                 (2.0, -1.0), (2.0, 1.0),
                 (4.0, -2.0), (4.0, 2.0),
                 (5.0, -1.0), (5.0, 1.0)]

    # Modifica os valores internos de forma aleatória até o valor máximo de 4 antes do embaralhamento
    for i in range(1, len(positions)):
        x, y = positions[i]
        # Exemplo: Modifica y para um valor aleatório entre y-2 e o mínimo entre y+2 e 4
        positions[i] = (x, round(uniform(-2.0, 2.0)))

    # Embaralha as posições excluindo a posição inicial (0, 0)
    #shuffle(positions[1:])

    return positions


def generate_graph(jogadores: List[Any], posicoes: List[Tuple[float, float]]):
    """Gera um grafo simples, sem arestas, e com os jogadores
    como vértices."""
    grafo = GrafoSimples()

    for jogador, posicao in zip(jogadores, posicoes):
        grafo.adiciona_vertice(jogador, posicao)

    return grafo

def update_positions():
    global posicoes, grafo

    posicoes = get_player_positions()
    grafo = generate_graph(jogadores, posicoes)
    pygame.time.set_timer(pygame.USEREVENT, 5000)  # Define um evento do Pygame para ocorrer a cada 5 segundos
    grafo = generate_graph(jogadores, posicoes)
    grafo.adiciona_aresta("Martinelli", "Jesus")
    grafo.adiciona_aresta("André", "Raphinha")
    grafo.adiciona_aresta("André", "Guimarães")
    grafo.adiciona_aresta("André", "Raphinha")
    grafo.adiciona_aresta("Rodrygo", "Raphinha")
    grafo.adiciona_aresta("Rodrygo", "Martinelli")
    grafo.adiciona_aresta("Royal", "André")
    grafo.adiciona_aresta("Marquinhos", "André")
    grafo.adiciona_aresta("Royal", "Rodrygo")
    grafo.visualizar()


if __name__ == "__main__":
    TAMANHO_TELA = (1600, 900)
    COR_CIRCULO = (255, 255, 255)

    jogadores = ["Alisson", "Royal", "Marquinhos", "Magalhães",
                 "Augusto", "André", "Guimarães", "Rodrygo",
                 "Raphinha", "Jesus", "Martinelli"]
    posicoes = get_player_positions()
    pygame.init()
    update_positions()

    grafo = generate_graph(jogadores, posicoes)
    grafo.adiciona_aresta("Martinelli", "Jesus")
    grafo.adiciona_aresta("André", "Raphinha")
    grafo.adiciona_aresta("André", "Guimarães")
    grafo.adiciona_aresta("André", "Raphinha")
    grafo.adiciona_aresta("Rodrygo", "Raphinha")
    grafo.adiciona_aresta("Rodrygo", "Martinelli")
    grafo.adiciona_aresta("Royal", "André")
    grafo.adiciona_aresta("Marquinhos", "André")
    grafo.adiciona_aresta("Royal", "Rodrygo")
    grafo.visualizar()

    #pygame.init()
    tela = pygame.display.set_mode(TAMANHO_TELA)
    interface = InterfaceDrawer(tela, "assets/pitch.jpg")

    interface.draw_background()
    interface.draw_edges(grafo, (255, 0, 0))
    interface.draw_players(grafo, COR_CIRCULO)
    #

    quit = False
    while not quit:
        quit = process_event_bus()
        
        # Atualiza a tela
        interface.draw_background()
        interface.draw_edges(grafo, (255, 0, 0))  # Desenha as linhas vermelhas
        interface.draw_players(grafo, COR_CIRCULO)

        pygame.display.flip()  # Atualiza a tela do Pygame
        pygame.time.Clock().tick(1)  # Controla a taxa de quadros
        
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:  # Verifica se ocorreu o evento definido pelo Pygame (a cada 5 segundos)
                update_positions() 

