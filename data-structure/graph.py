import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    """
    Uma classe que representa um grafo usando a biblioteca NetworkX para armazenar
    os dados do grafo e a biblioteca Matplotlib para visualização do grafo.
    """

    def __init__(self):
        """
        Inicializa um objeto Grafo com um grafo vazio.
        """
        self.grafo = nx.Graph()

    def adiciona_vertice(self, vertice):
        """
        Adiciona um vértice ao grafo.

        :param vertice: O rótulo do vértice a ser adicionado.
        """
        self.grafo.add_node(vertice)

    def adiciona_aresta(self, de, para, peso):
        """
        Adiciona uma aresta ponderada ao grafo.

        :param de: O rótulo do vértice de origem da aresta.
        :param para: O rótulo do vértice de destino da aresta.
        :param peso: O peso da aresta, que neste contexto pode representar a probabilidade
                     de sucesso de um passe entre os jogadores no campo de futebol.
        """
        self.grafo.add_edge(de, para, weight=peso)

    def visualizar(self, posicoes):
        """
        Visualiza o grafo com os vértices posicionados de acordo com o dicionário 'posicoes' fornecido.

        :param posicoes: Um dicionário onde as chaves são os rótulos dos vértices e os valores
                         são as coordenadas (x, y) para a posição de cada vértice no gráfico.
        """
        plt.figure(figsize=(12,7))
        nx.draw_networkx_nodes(self.grafo, posicoes, node_size=700, node_color='lightblue')
        nx.draw_networkx_labels(self.grafo, posicoes)
        pesos = nx.get_edge_attributes(self.grafo, 'weight')
        pesos_normalizados = [pesos[edge] * 5 for edge in self.grafo.edges()] 
        nx.draw_networkx_edges(self.grafo, posicoes, width=pesos_normalizados)
        nx.draw_networkx_edge_labels(self.grafo, posicoes, edge_labels=pesos)
        plt.title("Visualização do Campo de Futebol como Grafo")
        plt.show()

    def adiciona_arestas_completas(self, posicoes):
        """
        Conecta todos os vértices uns com os outros (grafo completo), com pesos inversamente
        proporcionais à distância euclidiana entre os vértices no gráfico.

        :param posicoes: Um dicionário de posições dos vértices como usado na função 'visualizar'.
        """
        for jogador1 in posicoes:
            for jogador2 in posicoes:
                if jogador1 != jogador2:
                    dist = self.distancia_euclidiana(posicoes[jogador1], posicoes[jogador2])
                    peso = 1 / dist
                    self.adiciona_aresta(jogador1, jogador2, round(peso, 2))

    def distancia_euclidiana(self, pos_a, pos_b):
        """
        Calcula a distância euclidiana entre dois pontos.

        :param pos_a: As coordenadas (x, y) do primeiro ponto.
        :param pos_b: As coordenadas (x, y) do segundo ponto.
        :return: A distância euclidiana entre os dois pontos.
        """
        return ((pos_a[0] - pos_b[0]) ** 2 + (pos_a[1] - pos_b[1]) ** 2) ** 0.5



g = Grafo()
jogadores = ['João Ricardo', 'Titi', 'Britez', 'Tinga', 'Bruno Pacheco',
             'Caio Alexandre', 'Zé Wellison', 'Caleb', 'Yago Pikachu',
             'Guilherme', 'Galhardo']



if __name__ == "__main__":
    for jogador in jogadores:
        g.adiciona_vertice(jogador)


    g.adiciona_aresta('João Ricardo', 'Titi', 0.9)
    g.adiciona_aresta('João Ricardo', 'Britez', 0.9)
    g.adiciona_aresta('Titi', 'Caio Alexandre', 0.8)
    g.adiciona_aresta('Britez', 'Zé Wellison', 0.8)
    g.adiciona_aresta('Tinga', 'Caleb', 0.8)
    g.adiciona_aresta('Bruno Pacheco', 'Yago Pikachu', 0.8)
    g.adiciona_aresta('Caio Alexandre', 'Guilherme', 0.7)
    g.adiciona_aresta('Zé Wellison', 'Guilherme', 0.7)
    g.adiciona_aresta('Caleb', 'Galhardo', 0.7)
    g.adiciona_aresta('Yago Pikachu', 'Galhardo', 0.7)
    posicoes = {
        'João Ricardo': (1, 1),  
        'Titi': (2, 2),           
        'Britez': (2, 4),
        'Tinga': (3, 1),
        'Bruno Pacheco': (3, 5),
        'Caio Alexandre': (4, 2), 
        'Zé Wellison': (4, 4),
        'Caleb': (5, 3),
        'Yago Pikachu': (6, 1),  
        'Guilherme': (6, 3),
        'Galhardo': (6, 5)
    }

    g.adiciona_arestas_completas(posicoes)
    g.visualizar(posicoes)
    plt.show()
    g.visualizar()
    plt.show()