from random import uniform
import pygame
import pygame_gui
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


def get_player_positions(formacao_time_1, formacao_time_2) -> List[Tuple[int, int]]:
    """Função temporária, que retorna um exemplo
    de posicionamento para os jogadores."""
    if(formacao_time_1 == "4-3-3"):
        posicao_time_1 = [(0, 0),
            (1, -2), (1, -1), (1, 1), (1, 2),

            (3, -2), (2, 0), (3, 2),
            (4, -2),(4, 0),(4,2)]
    if(formacao_time_1 == "4-4-2"):
        posicao_time_1 = [(0, 0),
            (1, -2), (1, -1), (1, 1), (1, 2),
            (2, -1), (2, 1),

            (3, -2), (3, 2),
            (4, -1), (4, 1)]
    if(formacao_time_1 == "4-5-1"):
        posicao_time_1 = [(0, 0),
            (1, -2), (1, -1), (1, 1), (1, 2),
            (2, -1), (2, 1),
            (2.5, 0),

            (3, -2), (3, 2),
            (4, 0)]

    if(formacao_time_2 == "4-3-3"):
        posicao_time_2 = [(5.2, 0),
            (4.2, -2), (4.2, -1), (4.2, 1), (4.2, 2),

            (2.2, -2), (3.2, 0), (2.2, 2),
            (1.2, -2),(1.2, 0),(1.2,2)]
    if(formacao_time_2 == "4-4-2"):
        posicao_time_2 = [(5.2, 0),
            (4.2, -2), (4.2, -1), (4.2, 1), (4.2, 2),
            (3.2, -1), (3.2, 1),

            (2.2, -2), (2.2, 2),
            (1.2, -1), (1.2, 1)]
    if(formacao_time_2 == "4-5-1"):
        posicao_time_2 = [(5.2, 0),
            (4.2, -2), (4.2, -1), (4.2, 1), (4.2, 2),
            (3.2, -1), (3.2, 1),
            (2.7, 0),

            (2.2, -2), (2.2, 2),
            (1.2, 0)]
        
    for i in range(1, len(posicao_time_1)):
        x, y = posicao_time_1[i]
        # Exemplo: Modifica y para um valor aleatório entre y-2 e o mínimo entre y+2 e 4
        posicao_time_1[i] = (x, round(uniform(-2.0, 2.0)))
    
    for i in range(1, len(posicao_time_2)):
        x, y = posicao_time_2[i]
        # Exemplo: Modifica y para um valor aleatório entre y-2 e o mínimo entre y+2 e 4
        posicao_time_2[i] = (x, round(uniform(-2.0, 2.0)))

    return posicao_time_1, posicao_time_2

def generate_graph(jogadores: List[Any], posicoes: List[Tuple[int, int]]):
    """Gera um grafo simples, sem arestas, e com os jogadores
    como vértices."""
    grafo = GrafoSimples()

    for jogador, posicao in zip(jogadores, posicoes):
        grafo.adiciona_vertice(jogador, posicao)

    return grafo


def update_positions(formacao_time_1, formacao_time_2):
    global posicoes_time_1, posicoes_time_2, grafo, grafo_two

    posicoes_time_1, posicoes_time_2 = get_player_positions(formacao_time_1, formacao_time_2)
    grafo = generate_graph(jogadores_time_1, posicoes_time_1)
    grafo.cria_grafo_completo()
    grafo.visualizar()

    grafo_two = generate_graph(jogadores_time_2, posicoes_time_2)
    grafo_two.visualizar()
    pygame.time.set_timer(pygame.USEREVENT, 5000)  # Define um evento do Pygame para ocorrer a cada 5 segundos


def main_menu(screen):
    """Exibe o menu inicial para seleção das formações com uma imagem de fundo."""
    pygame.init()

    tela_largura, tela_altura = screen.get_size()

    fundo = pygame.image.load('assets/init_background.jpeg')
    fundo = pygame.transform.scale(fundo, (tela_largura, tela_altura))

    largura_dropdown = 200
    altura_dropdown = 30
    largura_botao = 100
    altura_botao = 50
    espacamento = 20

    pos_x_botao = tela_largura // 2 - largura_botao // 2
    pos_y_botao = tela_altura // 2 - altura_botao // 2

    pos_x_dropdown1 = tela_largura // 2 - largura_dropdown - espacamento
    pos_x_dropdown2 = tela_largura // 2 + espacamento
    pos_y_dropdown = tela_altura // 2 - altura_dropdown // 2 - 100

    fonte = pygame.font.Font(None, 24)
    texto_time_1 = fonte.render('Time 1', True, pygame.Color('black'))
    texto_time_2 = fonte.render('Time 2', True, pygame.Color('black'))
    texto_time_1_rect = texto_time_1.get_rect(center=(pos_x_dropdown1 + largura_dropdown / 2, pos_y_dropdown - 15))
    texto_time_2_rect = texto_time_2.get_rect(center=(pos_x_dropdown2 + largura_dropdown / 2, pos_y_dropdown - 15))

    manager = pygame_gui.UIManager((tela_largura, tela_altura))

    dropdown_time_1 = pygame_gui.elements.UIDropDownMenu(
        options_list=["4-4-2", "4-3-3", "4-5-1"],
        starting_option="4-4-2",
        relative_rect=pygame.Rect((pos_x_dropdown1, pos_y_dropdown), (largura_dropdown, altura_dropdown)),
        manager=manager)

    dropdown_time_2 = pygame_gui.elements.UIDropDownMenu(
        options_list=["4-4-2", "4-3-3", "4-5-1"],
        starting_option="4-4-2",
        relative_rect=pygame.Rect((pos_x_dropdown2, pos_y_dropdown), (largura_dropdown, altura_dropdown)),
        manager=manager)

    confirm_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((pos_x_botao, pos_y_botao), (largura_botao, altura_botao)),
        text='Confirmar',
        manager=manager)

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60)/1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == confirm_button:
                    return dropdown_time_1.selected_option, dropdown_time_2.selected_option

            manager.process_events(event)

        manager.update(time_delta)

        screen.blit(fundo, (0, 0))

        screen.blit(texto_time_1, texto_time_1_rect)
        screen.blit(texto_time_2, texto_time_2_rect)

        manager.draw_ui(screen)

        pygame.display.update()

    pygame.quit()



if __name__ == "__main__":
    TAMANHO_TELA = (1600, 900)
    COR_CIRCULO = (255, 255, 255)

    pygame.init()
    tela = pygame.display.set_mode((800, 600))
    formacao_time_1, formacao_time_2 = main_menu(tela)

    jogadores_time_1 = ["Alisson", "Royal", "Marquinhos", "Magalhães",
                 "Augusto", "André", "Guimarães", "Rodrygo",
                 "Raphinha", "Jesus", "Martinelli"]
    jogadores_time_2 = [
    "Bruno", "Carlos", "Daniel", "Eduardo", "Fernando", "Gabriel",
    "Henrique", "Igor", "João", "Lucas", "Matheus"]
    posicoes_time_1, posicoes_time_2 = get_player_positions(formacao_time_1, formacao_time_2)

    pygame.init()
    update_positions(formacao_time_1, formacao_time_2)

    grafo = generate_graph(jogadores_time_1, posicoes_time_1)
    grafo.cria_grafo_completo()
    grafo.visualizar()

    grafo_two = generate_graph(jogadores_time_2, posicoes_time_2)
    grafo_two.visualizar()

    pygame.init()
    tela = pygame.display.set_mode(TAMANHO_TELA)
    interface = InterfaceDrawer(tela, "assets/pitch.jpg")

    interface.draw_background()
    interface.draw_edges(grafo, (255, 0, 0))
    interface.draw_edges(grafo_two, (255, 0, 0))
    interface.draw_players(grafo, COR_CIRCULO)
    interface.draw_players(grafo_two, (255, 255, 0))

    quit = False
    clock = pygame.time.Clock()

    while not quit:
        quit = process_event_bus()

        interface.draw_background()
        interface.draw_edges(grafo, (255, 0, 0))
        interface.draw_edges(grafo_two, (255, 0, 0))
        interface.draw_players(grafo, COR_CIRCULO)
        interface.draw_players(grafo_two, (255, 255, 0))

        pygame.display.flip()
        clock.tick(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
            elif event.type == pygame.USEREVENT:
                update_positions(formacao_time_1, formacao_time_2)

    pygame.quit()
