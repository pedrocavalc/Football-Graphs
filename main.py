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


def get_player_positions() -> List[Tuple[int, int]]:
    """Função temporária, que retorna um exemplo
    de posicionamento para os jogadores."""
    return [(0, 0),
            (1, -2), (1, -1), (1, 1), (1, 2),
            (2, -1), (2, 1),

            (4, -2), (4, 2),
            (5, -1), (5, 1)]


def generate_graph(jogadores: List[Any], posicoes: List[Tuple[int, int]]):
    """Gera um grafo simples, sem arestas, e com os jogadores
    como vértices."""
    grafo = GrafoSimples()

    for jogador, posicao in zip(jogadores, posicoes):
        grafo.adiciona_vertice(jogador, posicao)

    return grafo


if __name__ == "__main__":
    TAMANHO_TELA = (1600, 900)
    COR_CIRCULO = (255, 255, 255)

    jogadores = ["Alisson", "Royal", "Marquinhos", "Magalhães",
                 "Augusto", "André", "Guimarães", "Rodrygo",
                 "Raphinha", "Jesus", "Martinelli"]
    posicoes = get_player_positions()

    grafo = generate_graph(jogadores, posicoes)
    grafo.adiciona_aresta("Martinelli", "Jesus", 1)
    grafo.adiciona_aresta("André", "Raphinha", 1)
    grafo.adiciona_aresta("André", "Guimarães", 1)
    grafo.adiciona_aresta("André", "Raphinha", 1)
    grafo.adiciona_aresta("Rodrygo", "Raphinha", 1)
    grafo.adiciona_aresta("Rodrygo", "Martinelli", 1)
    grafo.adiciona_aresta("Royal", "André", 1)
    grafo.adiciona_aresta("Marquinhos", "André", 1)
    grafo.adiciona_aresta("Royal", "Rodrygo", 1)
    grafo.visualizar()

    pygame.init()
    tela = pygame.display.set_mode(TAMANHO_TELA)
    interface = InterfaceDrawer(tela, "assets/pitch.jpg")

    interface.draw_background()
    interface.draw_edges(grafo, (255, 0, 0))
    interface.draw_players(grafo, COR_CIRCULO)

    quit = False
    while not quit:
        quit = process_event_bus()
