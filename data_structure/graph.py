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


g = GrafoSimples()
g.adiciona_vertice("A", (100, 200))
g.adiciona_vertice("B", (150, 250))
g.adiciona_aresta("A", "B", 1)
g.adiciona_aresta("B", "A", 2)

g.visualizar()

print(g.get_posicao_vertice("A")) 
print(g.get_posicao_vertice("C")) 
