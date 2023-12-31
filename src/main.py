import copy
import random
from Grafo import Graph
from DefineVertex import define_vertex
from CaminhoCritico import CalculaSequenciaCritica
from RepresentaçãoGrafica import print_graficamente

def print_sequencia(lista):
    for m in lista[:len(lista)-1]:
        print(f"{m} -> ", end = "")

    print(f"{lista[-1]}.", end = "")

#Lê o arquivo com todas as diciplinas e seus pré-requisitos
arquivo_diciplinas = open("src/DATA/DiciplinasCIC.txt")
materias = arquivo_diciplinas.read().split("\n")

#Embaralha as matérias para simular um ambiente mais realista
random.shuffle(materias)

#Começo efeitvo do código
grafo = Graph()

#Define os Vêrtices do Grafo, sua incidência e sua saida
define_vertex(grafo, materias)

#Define dois possíveis caminhos críticos com seu número de matérias
sequencia_apc, name_max_apc = CalculaSequenciaCritica(copy.deepcopy(grafo), grafo.getVertex("CIC0004"))

sequencia_c1, name_max_c1 = CalculaSequenciaCritica(copy.deepcopy(grafo), grafo.getVertex("MAT0025"))

#Impressão dos resultados
print("--------------------------------------")
print("Bacharelado em Ciência da Computação:")
print()
print(f"O caminho crítico começando por apc tem {len(sequencia_apc)} matérias.")
print(f"Com sequência: ", end = "")
print_sequencia(sequencia_apc)
print()
print()
print(f"O caminho crítico começando por cáclculo 1 tem {len(sequencia_c1)} matérias")
print(f"Com sequência: ")
print_sequencia(sequencia_c1)

print_graficamente(copy.deepcopy(grafo))