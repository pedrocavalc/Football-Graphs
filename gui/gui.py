import pygame
from typing import Tuple, List

from data_structure.graph import GrafoSimples


class InterfaceDrawer:
    """Classe que abstrai as funções de desenho do PyGame."""

    def __init__(self, tela: pygame.surface, background_path: str):
        """Inicializa um InterfaceDrawer.
        
        args:
            tela (pygame.surface): Uma superfície do PyGame para desenhar sobre.
            background_path (str): Um path para uma imagem que servirá de fundo.
        """
        self.screen = tela
        self.font = pygame.font.SysFont(None, 24)

        background = pygame.image.load(background_path)
        self.background = pygame.transform.scale(background, tela.get_size())

    def draw_players(self, grafo: GrafoSimples, cor_jogador: pygame.Vector3):
        """Dado um grafo simples, desenha os vértices do grafo na tela do PyGame.
        
        args:
            grafo (GrafoSimples): um grafo para desenhar.
            cor_jogador (pygame.Vector3): uma cor, em RGB, para o jogador.
        """
        for vertice in grafo.vertices.values():
            posicao = posicao_para_coordenada(vertice.posicao, self.screen.get_size())
            pygame.draw.circle(self.screen, cor_jogador, posicao, 50)

            text = self.font.render(vertice.nome, True, (255, 0, 0))
            text_rect = text.get_rect(center=posicao)
            self.screen.blit(text, text_rect)

        pygame.display.update()

    def draw_edges(self, grafo: GrafoSimples, cor_linha: pygame.Vector3):
        """Dado um grafo simples, desenha as arestas do grafo na tela do PyGame.
        
        args:
            grafo (GrafoSimples): um grafo para desenhar.
            cor_linha (pygame.Vector3): uma cor, em RGB, para as linhas
        """
        for vertice in grafo.vertices.values():
            for arestas in vertice.arestas:
                pos_inicial = posicao_para_coordenada(vertice.posicao, self.screen.get_size())
                pos_final = posicao_para_coordenada(arestas[0].posicao, self.screen.get_size())
                pygame.draw.line(self.screen, cor_linha, pos_inicial, pos_final, 10)

        pygame.display.update()

    def draw_background(self):
        """Desenha o fundo designado na tela do PyGame."""
        black = (0, 0, 0)
        self.screen.fill(black)
        self.screen.blit(self.background, (0, 0))


def posicoes_para_coordenadas(posicoes: List[pygame.Vector2], tamanho_tela: Tuple[int, int]) -> List[pygame.Vector2]:
    """Converte uma lista de posições arbitrárias em posições em pixel, para
    serem desenhadas pelo pygame.
    """
    x0 = 200
    y0 = tamanho_tela[1] / 2
    step_x = (tamanho_tela[0] - x0) / 6
    step_y = (tamanho_tela[1] - 100) / 5
    return [(x0 + step_x*x, y0 + step_y*y) for x, y in posicoes]


def posicao_para_coordenada(posicao: pygame.Vector2, tamanho_tela: Tuple[int, int]) -> pygame.Vector2:
    """Converte uma posição arbitrária em uma posição em pixel, para ser
    desenhada pelo pygame.
    """
    x0 = 200
    y0 = tamanho_tela[1] / 2
    step_x = (tamanho_tela[0] - x0) / 6
    step_y = (tamanho_tela[1] - 100) / 5
    return (x0 + step_x*posicao[0], y0 + step_y*posicao[1])
