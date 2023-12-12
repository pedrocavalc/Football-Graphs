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
        self.font = pygame.font.SysFont(None, 15)
        self.button_font = pygame.font.SysFont(None, 80)
        self.score = 0

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
            pygame.draw.circle(self.screen, cor_jogador, posicao, 30)

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
                pygame.draw.line(self.screen, cor_linha, pos_inicial, pos_final, 5)

        pygame.display.update()

    def draw_path(self, grafo: GrafoSimples, caminho: List[str], cor_linha: pygame.Vector3):
        """Dado um grafo simples e um caminho, desenha as arestas do caminho na tela do PyGame.
        
        args:
            grafo (GrafoSimples): um grafo para desenhar.
            caminho (List[str]): uma lista de nomes de vértices representando o caminho.
            cor_linha (pygame.Vector3): uma cor, em RGB, para as linhas do caminho.
        """
        for i in range(len(caminho) - 1):
            vertice_atual = grafo.vertices[caminho[i]]
            vertice_proximo = grafo.vertices[caminho[i + 1]]

            pos_inicial = posicao_para_coordenada(vertice_atual.posicao, self.screen.get_size())
            pos_final = posicao_para_coordenada(vertice_proximo.posicao, self.screen.get_size())
            pygame.draw.line(self.screen, cor_linha, pos_inicial, pos_final, 5)

        pygame.display.update()

    def draw_background(self):
        """Desenha o fundo designado na tela do PyGame."""
        black = (0, 0, 0)
        self.screen.fill(black)
        self.screen.blit(self.background, (0, 0))
        
    def draw_button(self, texto: str, inverted: bool):
        """Desenha um botão com o texto enviado como argumento"""
        tamanho_tela = self.screen.get_size()
        button_width = tamanho_tela[0] / 6
        button_height = tamanho_tela[1] / 6
        
        pos_x = tamanho_tela[0] - button_width if inverted else 0
        pos_y = tamanho_tela[1] - button_height
        
        fundo = pygame.Rect(pos_x, pos_y, button_width, button_height)
        pygame.draw.rect(self.screen, (255, 255, 255), fundo)
        text = self.button_font.render(texto, True, (0, 0, 0))
        text_rect = text.get_rect(center=fundo.center)
        self.screen.blit(text, text_rect)
        
        pygame.display.update()
        
    def draw_score(self):
        placar = pygame.image.load("assets/placar.png")
        pos_x = (self.screen.get_size()[0] / 2) - placar.get_width() / 2
        pos_y = 0
        self.screen.blit(placar, (pos_x, pos_y))
        
        text_pos_x = self.screen.get_size()[0] / 2
        text_pos_y = 45
        
        gols_casa = self.button_font.render(str(self.score), True, (0, 0, 0))
        text_rect = gols_casa.get_rect(center=(text_pos_x - 40, text_pos_y))
        self.screen.blit(gols_casa, text_rect)
        
        gols_fora = self.button_font.render("0", True, (0, 0, 0))
        text_rect = gols_fora.get_rect(center=(text_pos_x + 40, text_pos_y))
        self.screen.blit(gols_fora, text_rect)
        

        pygame.display.update()


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
