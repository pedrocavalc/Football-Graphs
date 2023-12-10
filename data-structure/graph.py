import matplotlib.pyplot as plt
import networkx as nx

class GrafoSimples:
    """
    Representa um grafo simples direcionado com vértices posicionados.

    Atributos:
    vertices (dict): Um dicionário que mapeia o nome do vértice para o objeto Vertice correspondente.
    """

    class Vertice:
        """
        Representa um vértice em um grafo.

        Atributos:
        nome (str): O nome identificador do vértice.
        posicao (tuple): A posição do vértice, geralmente como um par de coordenadas (x, y).
        arestas (list): Uma lista de tuplas representando as arestas e seus pesos para outros vértices.
        """

        def __init__(self, nome, posicao):
            """
            Inicializa um novo vértice com um nome e posição.

            Parâmetros:
            nome (str): O nome do vértice.
            posicao (tuple): A posição do vértice.
            """
            self.nome = nome
            self.posicao = posicao
            self.arestas = []

    def __init__(self):
        """
        Inicializa um novo grafo simples sem vértices.
        """
        self.vertices = {}  # Armazena os objetos Vertice
    
    def construir_grafo_networkx(self):
        """
        Constrói um objeto grafo NetworkX a partir da estrutura atual do GrafoSimples.
        """
        grafo_nx = nx.DiGraph()  # Criar um grafo direcionado com NetworkX
        for vertice in self.vertices.values():
            grafo_nx.add_node(vertice.nome, pos=vertice.posicao)
            for vizinho, peso in vertice.arestas:
                grafo_nx.add_edge(vertice.nome, vizinho.nome, weight=peso)
        return grafo_nx

    def adiciona_vertice(self, nome, posicao):
        """
        Adiciona um novo vértice ao grafo.

        Parâmetros:
        nome (str): O nome do vértice a ser adicionado.
        posicao (tuple): A posição do vértice a ser adicionado.
        """
        if nome not in self.vertices:
            self.vertices[nome] = GrafoSimples.Vertice(nome, posicao)

    def adiciona_aresta(self, de, para, peso):
        """
        Adiciona uma aresta direcionada e ponderada entre dois vértices no grafo.

        Parâmetros:
        de (str): O nome do vértice de origem.
        para (str): O nome do vértice de destino.
        peso (int/float): O peso da aresta.
        """
        if de in self.vertices and para in self.vertices:
            self.vertices[de].arestas.append((self.vertices[para], peso))

    def visualizar(self):
        """
        Imprime uma representação textual do grafo, mostrando vértices, suas posições e arestas.
        """
        for vertice in self.vertices.values():
            print(f"Vértice {vertice.nome} na posição {vertice.posicao}:")
            for vizinho, peso in vertice.arestas:
                print(f"  --({peso})--> {vizinho.nome} na posição {vizinho.posicao}")

    def get_posicao_vertice(self, nome):
        """
        Retorna a posição de um vértice específico.

        Parâmetros:
        nome (str): O nome do vértice.

        Retorna:
        tuple: A posição do vértice, ou uma mensagem de erro se o vértice não for encontrado.
        """
        if nome in self.vertices:
            return self.vertices[nome].posicao
        else:
            return "Vértice não encontrado"

    def plotar_grafo(self):
        """
        Plota o grafo visualmente usando matplotlib.
        """
        fig, ax = plt.subplots()

        # Desenhar vértices
        for vertice in self.vertices.values():
            ax.scatter(*vertice.posicao, s=100)  # s é o tamanho do ponto
            ax.text(*vertice.posicao, vertice.nome, fontsize=12, ha='right')

        # Desenhar arestas
        for vertice in self.vertices.values():
            for vizinho, peso in vertice.arestas:
                ax.arrow(
                    *vertice.posicao,
                    *(vizinho.posicao[0] - vertice.posicao[0], vizinho.posicao[1] - vertice.posicao[1]),
                    head_width=5,
                    head_length=10,
                    fc='lightblue',
                    ec='black'
                )

        plt.show()


    def encontra_caminho_mais_curto(self, origem, destino):
        """
        Encontra o caminho mais curto entre dois vértices usando o algoritmo de Dijkstra.

        :param origem: O nome do vértice de origem.
        :param destino: O nome do vértice de destino.
        :return: Uma lista de vértices representando o caminho mais curto.
        """
        grafo_nx = self.construir_grafo_networkx()
        try:
            return nx.dijkstra_path(grafo_nx, origem, destino)
        except nx.NetworkXNoPath:
            return "Não há caminho disponível."


g = GrafoSimples()
g.adiciona_vertice("A", (100, 200))
g.adiciona_vertice("B", (150, 250))
g.adiciona_vertice("C", (300, 50))
g.adiciona_vertice("D", (350, 300))
g.adiciona_vertice("E", (230, 200))
g.adiciona_aresta("A", "B", 1)
g.adiciona_aresta("A", "C", 6)
g.adiciona_aresta("A", "D", 8)
g.adiciona_aresta("A", "E", 2)
g.adiciona_aresta("B", "A", 1)
g.adiciona_aresta("B", "C", 6)
g.adiciona_aresta("B", "D", 5)
g.adiciona_aresta("B", "E", 2)
g.adiciona_aresta("C", "A", 6)
g.adiciona_aresta("C", "B", 6)
g.adiciona_aresta("C", "D", 8)
g.adiciona_aresta("C", "E", 3)
g.adiciona_aresta("D", "A", 8)
g.adiciona_aresta("D", "B", 5)
g.adiciona_aresta("D", "C", 8)
g.adiciona_aresta("D", "E", 3)
g.adiciona_aresta("E", "A", 2)
g.adiciona_aresta("E", "B", 2)
g.adiciona_aresta("E", "C", 3)
g.adiciona_aresta("E", "D", 3)





print(g.get_posicao_vertice("A"))
print(g.get_posicao_vertice("C"))
print(g.encontra_caminho_mais_curto('A', 'C'))
g.visualizar()
g.plotar_grafo()



